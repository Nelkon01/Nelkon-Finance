from collections import defaultdict
from datetime import datetime

from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import func, extract

from budgetmanager import app, db
from budgetmanager.models import Users, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses


@app.route('/')
def home():
    if "user_id" in session:
        return redirect(url_for('plan'))
    return render_template('home.html')


month_name_to_number = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12',
}


# Plan route
@app.route('/plan')
@login_required
def plan():
    # check if user is logged in
    if "user_id" in session:
        try:
            user_id = session["user_id"]

            # get the current user
            curr_user = Users.query.get(user_id)

            # Query the budget incomes and expenses for the user
            budget_incomes = BudgetedIncome.query.filter_by(user_id=user_id).order_by(
                BudgetedIncome.year).all()
            budget_expenses = BudgetedExpenses.query.filter_by(user_id=user_id).order_by(
                BudgetedExpenses.year).all()

            # sort budget income and expenses by month using month_name_to_number
            budget_incomes.sort(key=lambda x: month_name_to_number.get(x.month_name))
            budget_expenses.sort(key=lambda x: month_name_to_number.get(x.month_name))

            # Group budget incomes and expenses by month and year into a dict
            budget_incomes_by_month = defaultdict(list)
            for budget_income in budget_incomes:
                month_year = (budget_income.month_name, budget_income.year)
                budget_incomes_by_month[month_year].append(budget_income)

            budget_expenses_by_month = defaultdict(list)
            for budget_expense in budget_expenses:
                month_year = (budget_expense.month_name, budget_expense.year)
                budget_expenses_by_month[month_year].append(budget_expense)

            return render_template('plan.html', user=curr_user, budget_incomes=budget_incomes,
                                   budget_expenses=budget_expenses, budget_incomes_by_month=budget_incomes_by_month,
                                   budget_expenses_by_month=budget_expenses_by_month)
        except Exception as e:
            flash("An error occurred while loading your budget data. Please try again later.", "error")
            app.logger.error(f"Error loading user data: {str(e)}")
            return render_template('error.html', error_message=f"An Error occurred while loading your"
                                                               f" plan data. Please try again later.")
    else:
        flash("You must be logged in to access this page.", "error")
        return redirect(url_for("login"))




@app.route('/track')
@login_required
def track():
    if "user_id" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)
        try:
            # query and filter the actual incomes and expenses
            actual_incomes = ActualIncome.query.filter_by(user_id=user_id).order_by(ActualIncome.date).all()
            actual_expenses = ActualExpenses.query.filter_by(user_id=user_id).order_by(ActualExpenses.date).all()

            actual_incomes_by_month = defaultdict(list)
            for actual_income in actual_incomes:
                month_year = (actual_income.date.strftime("%B"), actual_income.date.year)
                actual_incomes_by_month[month_year].append(actual_income)

            actual_expenses_by_month = defaultdict(list)
            for actual_expense in actual_expenses:
                month_year = (actual_expense.date.strftime("%B"), actual_expense.date.year)
                actual_expenses_by_month[month_year].append(actual_expense)

            return render_template('track.html', user=curr_user, actual_incomes=actual_incomes,
                                   actual_expenses=actual_expenses, actual_incomes_by_month=actual_incomes_by_month,
                                   actual_expenses_by_month=actual_expenses_by_month)
        except Exception as e:
            app.logger.error(f"An error occurred: {str(e)}")
            return render_template('error.html', error_message=f"An Error occurred while loading your"
                                                               f" tracking data. Please try again later.")
    else:
        return redirect(url_for("login"))


# Signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        password = request.form.get("password")
        email = request.form.get("email")

        # Basic Form Validation
        if not username or not firstname or not lastname or not password or not email:
            flash('All fields are required', 'error')
            return redirect(url_for('signup'))

        # Check if username or email already exists
        user_check = Users.query.filter_by(username=username).first()
        email_check = Users.query.filter_by(email=email).first()

        if user_check:
            flash('Username already exists', 'error')
            return redirect(url_for('login'))
        elif email_check:
            flash('Email already exists', 'error')
            return redirect(url_for('login'))

        # Hash Password
        encrypted_password = generate_password_hash(password, method="sha256")

        # Create new user
        new_user = Users(
            username=username,
            firstname=firstname,
            lastname=lastname,
            password=encrypted_password,
            email=email
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred during the registration. Please try again later')
            app.logger.error(f"Registration error: {str(e)}")
            return redirect(url_for('error.html'))
    # If GET request, render the signup form
    return redirect(url_for('signup'))


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        identifier = request.form['identifier']
        password = request.form['password']

        if not identifier or not password:
            flash('Please enter both username or email and password', 'error')
            return redirect(url_for('login'))

        curr_user = Users.query.filter(
            (Users.username == identifier) | (Users.email == identifier)
        ).first()
        if curr_user and check_password_hash(curr_user.password, password):
            login_user(curr_user)
            flash('Logged in successfully!', 'success')
            session.permanent = True
            session["user_id"] = curr_user.id
            next_page = request.args.get('next') or 'home'
            return redirect(url_for(next_page))
        else:
            flash('Invalid username/email or password', 'error')

    if current_user.is_authenticated:
        flash('You are already logged in!', 'success')
        return redirect(url_for('plan'))

    return render_template('login.html')


@app.route('/add_budget_income', methods=['POST', 'GET'])
@login_required
def add_budget_income():
    #     collect form data from add_budget_expense form
    month_name = request.form.get('month_name')
    year = request.form.get('year')
    income_name = request.form.get('income_name')
    budget_amount = request.form.get('budget_amount')

    # form validation
    if not (month_name and year and income_name and budget_amount):
        flash('All fields are required', 'error')
        return redirect(url_for('plan'))

    try:
        #     convert year and budget to their respective types
        year = int(year)
        budget_amount = float(budget_amount)

        # Ensure user is the owner by checking their id
        if current_user.id:
            # New budget income record
            budgeted_income = BudgetedIncome(
                income_name=income_name,
                user_id=current_user.id,
                month_name=month_name,
                year=year,
                budget_amount=budget_amount
            )
            db.session.add(budgeted_income)
            db.session.commit()

            flash('Budget Income added successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while adding the budget income. Please try again later.' 'error')
        app.logger.error(f"Error adding budget income: {str(e)}")
        return render_template('error.html')

    return redirect(url_for('plan'))


@app.route('/edit_budget_income/<int:income_id>', methods=['POST', 'GET'])
@login_required
def edit_budget_income(income_id):
    # Get the budget income record by income id
    budget_income = BudgetedIncome.query.get_or_404(income_id)

    if budget_income.user_id != current_user.id:
        flash("You don't have the permission to edit this budget income.", 'error')
        return render_template('error.html', error_message='Permission Denied')

    if request.method == 'POST':
        #     collect form data from add_budget_expense form
        month_name = request.form.get('month_name')
        year = request.form.get('year')
        income_name = request.form.get('income_name')
        budget_amount = request.form.get('budget_amount')

        try:
            year = int(year)
            budget_amount = float(budget_amount)

            # update the budget income values of that id
            budget_income.month_name = month_name
            budget_income.year = year
            budget_income.income_name = income_name
            budget_income.budget_amount = budget_amount

            db.session.commit()
            flash("Budget Income updated Successfully", 'success')

        except ValueError as e:
            flash("Invalid data types provided. Please check your input", 'error')
            app.logger.error(f"Error updating budget expense: {str(e)}")
            return render_template('error.html', error_message=f'{str(e)}')

        except AttributeError as e:
            flash('An error occurred, please try again later')
            app.logger.error(f"Error updating budget expense: {str(e)}")
            return render_template('error.html', error_message=f'{str(e)}')

        except SQLAlchemyError as e:
            db.session.rollback()
            flash("An error occurred while updating the budget income. Please try again later.", 'error')
            app.logger.error(f"Error updating budget expense: {str(e)}")
            return render_template("error.html", error_message=f"{str(e)}")

    return redirect(url_for('plan'))


@app.route('/delete_budget_income/<int:income_id>', methods=['POST', 'GET'])
@login_required
def delete_budget_income(income_id):
    budget_income = BudgetedIncome.query.get_or_404(income_id)

    # Check if the user trying to delete a budget income is the owner
    if budget_income.user_id != current_user.id:
        flash("You don't have permission to delete this budget income.", 'error')
        return render_template('error.html', error_message='Permission Denied')

    try:
        db.session.delete(budget_income)
        db.session.commit()
        flash('Budget Income Deleted Successfully', 'success')
        return redirect(url_for('plan'))
    except SQLAlchemyError as e:
        db.session.rollback()
        flash("An error occurred while deleting the budget income. Please try again later")
        app.logger.error(f"Error deleting budget income: {str(e)}")
        return redirect(url_for('plan'))


@app.route('/add_budget_expense', methods=['POST', 'GET'])
@login_required
def add_budget_expense():
    #     collect form data from add_budget_expense form
    month_name = request.form.get('month_name')
    year = request.form.get('year')
    category_name = request.form.get('category_name')
    budget_amount = request.form.get('budget_amount')

    # form validation
    if not (month_name and year and category_name and budget_amount):
        flash('All fields are required', 'error')
        return redirect(url_for('plan'))

    try:
        #     convert year and budget to their respective types
        year = int(year)
        budget_amount = float(budget_amount)

        # Ensure user is the owner by checking their ID
        if current_user.id:
            budgeted_expense = BudgetedExpenses(
                category_name=category_name,
                user_id=current_user.id,
                month_name=month_name,
                year=year,
                budget_amount=budget_amount
            )
            db.session.add(budgeted_expense)
            db.session.commit()

            flash('Budget Expense added successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while adding the budget expense. Please try again later.', 'error')
        app.logger.error(f"Error adding budget expense: {str(e)}")
        return render_template('error.html')

    return redirect(url_for('plan'))


@app.route('/edit_budget_expense/<int:expense_id>', methods=['POST', 'GET'])
@login_required
def edit_budget_expense(expense_id):
    #     Get budget expenses by id
    budget_expenses = BudgetedExpenses.query.get_or_404(expense_id)

    if budget_expenses.user_id != current_user.id:
        flash("You don't have the permission to edit this budget expense.", 'error')
        return render_template('error.html', error_message='Permission Denied')

    if request.method == 'POST':
        #   Collect form data from form
        month_name = request.form.get('month_name')
        year = request.form.get('year')
        category_name = request.form.get('category_name')
        budget_amount = request.form.get('budget_amount')

        try:
            # Validate data types and perform updates
            year = int(year)
            budget_amount = float(budget_amount)

            #   update the budget expense values
            budget_expenses.month_name = month_name
            budget_expenses.year = year
            budget_expenses.category_name = category_name
            budget_expenses.budget_amount = budget_amount

            db.session.commit()
            flash("Budget Expense updated Successfully", 'success')
        except ValueError as e:
            flash("Invalid datat types provided. Please check your input", 'error')

        except SQLAlchemyError as e:
            db.session.rollback()
            flash("An error occurred while updating the budget expense. Please try again later.", 'error')
            app.logger.error(f"Error updating budget expense: {str(e)}")
            return render_template('error.html', error_message='An error occurred')

    return redirect(url_for('plan'))


@app.route('/delete_budget_expense/<int:expense_id>', methods=['POST', 'GET'])
@login_required
def delete_budget_expense(expense_id):
    budget_expense = BudgetedExpenses.query.get_or_404(expense_id)

    # Check if the user trying to delete a budget income is the owner
    if budget_expense.user_id != current_user.id:
        flash("You don't have permission to delete this budget expense.", 'error')
        return render_template('error.html', error_message='Permission Denied')

    try:
        db.session.delete(budget_expense)
        db.session.commit()
        flash('Budget Expense Deleted Successfully', 'success')
        return redirect(url_for('plan'))
    except SQLAlchemyError as e:
        db.session.rollback()
        flash("An error occurred while deleting the budget income. Please try again later")
        app.logger.error(f"Error deleting budget expense: {str(e)}")
        return redirect(url_for('plan'))


@app.route('/add_actual_expense', methods=['POST', 'GET'])
@login_required
def add_actual_expense():
    #     collect form data from add_actual_expense form
    date_str = request.form.get('date')
    expense_name = request.form.get('expense_name')
    category_name = request.form.get('category_name')
    actual_amount = request.form.get('actual_amount')

    # form validation
    if not (date_str and expense_name and category_name and actual_amount):
        flash('All fields are required', 'error')
        return redirect(url_for('track'))
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        if current_user.id:
            actual_expense = ActualExpenses(
                category_name=category_name,
                user_id=current_user.id,
                date=date,
                actual_amount=actual_amount,
                expense_name=expense_name
            )
            db.session.add(actual_expense)
            db.session.commit()

            flash('Actual Expense added successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while adding your actual expense. Please try again later.', 'error')
        app.logger.error(f"Error adding actual expense: {str(e)}")
        return render_template('error.html', error_message=f'An error occurred while adding your '
                                                           f'actual expense. Please try again later')
    return redirect(url_for('track'))


@app.route('/edit_actual_expense/<int:expense_id>', methods=['POST', 'GET'])
@login_required
def edit_actual_expense(expense_id):
    #   Get Actual Expenses by ID
    actual_expense = ActualExpenses.query.get_or_404(expense_id)

    if actual_expense.user_id != current_user.id:
        flash("You don't have the permission to edit this actual expense.", 'error')
        return render_template('error.html', error_message='Permission Denied')

    if request.method == 'POST':
        #   collect data from form
        date = request.form.get('date')
        expense_name = request.form.get('expense_name')
        category_name = request.form.get('category_name')
        actual_amount = request.form.get('actual_amount')

        try:
            actual_amount = float(actual_amount)
            #         update values
            actual_expense.date = datetime.strptime(date, "%d/%m/%Y")
            actual_expense.expense_name = expense_name
            actual_expense.category_name = category_name
            actual_expense.actual_amount = actual_amount

            db.session.commit()
            flash('Actual Expense Updated Successfully', 'success')
        except ValueError as e:
            flash("Invalid data types provided. Please check your input", 'error')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash("An error occurred while updating the budget expense. Please try again later.", 'error')
            app.logger.error(f"Error updating budget expense: {str(e)}")
            return render_template('error.html', error_message='An error occurred')

    return redirect(url_for('track'))


@app.route('/delete_actual_expense/<int:expense_id>', methods=['POST', 'GET'])
@login_required
def delete_actual_expense(expense_id):
    actual_expense = ActualExpenses.query.get_or_404(expense_id)

    # Check if the user trying to delete a budget income is the owner
    if actual_expense.user_id != current_user.id:
        flash("You don't have permission to delete this data.", 'error')
        return render_template('error.html', error_message='Permission Denied')

    try:
        db.session.delete(actual_expense)
        db.session.commit()
        flash('Actual Expense Deleted Successfully', 'success')
        return redirect(url_for('track'))
    except SQLAlchemyError as e:
        db.session.rollback()
        flash("An error occurred while deleting the actual expense. Please try again later.", 'error')
        app.logger.error(f"Error deleting the actual expense: {str(e)}")
        return redirect(url_for('track'))


# Add Actual Income route
@app.route('/add_actual_income', methods=['POST', 'GET'])
@login_required
def add_actual_income():
    #     collect form data from add_actual_expense form
    date_str = request.form.get('date')
    income_name = request.form.get('income_name')
    actual_amount = request.form.get('actual_amount')

    if not (date_str and income_name and actual_amount):
        flash('All fields are required', 'error')
        return redirect(url_for('track'))
    try:
        date = datetime.strptime(date_str, "%d/%m/%Y")
        actual_income = ActualIncome(
            income_name=income_name,
            user_id=current_user.id,
            date=date,
            actual_amount=actual_amount,
        )
        db.session.add(actual_income)
        db.session.commit()
        flash('Actual Expense added successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while adding your actual income. Please try again later.', 'error')
        app.logger.error(f"Error adding actual expense: {str(e)}")
        return render_template('error.html', error_message=f'An error occurred while adding your '
                                                           f'actual income. Please try again later')
    return redirect(url_for('track'))


@app.route('/edit_actual_income/<int:income_id>', methods=['POST', 'GET'])
@login_required
def edit_actual_income(income_id):
    #   Get Actual Income by ID
    actual_income = ActualIncome.query.get_or_404(income_id)

    if actual_income.user_id != current_user.id:
        flash("You don't have the permission to edit this actual expense.", 'error')
        return render_template('error.html', error_message='Permission Denied')

    if request.method == 'POST':
        #   collect data from form
        date = request.form.get('date')
        income_name = request.form.get('income_name')
        actual_amount = request.form.get('actual_amount')

        try:
            #         update values
            actual_income.date = datetime.strptime(date, "%d/%m/%Y")
            actual_income.income_name = income_name
            actual_income.actual_amount = actual_amount

            db.session.commit()
            flash('Actual Expense Updated Successfully', 'success')
        except ValueError as e:
            flash("Invalid data types provided. Please check your input", 'error')
        except SQLAlchemyError as e:
            db.session.rollback()
            flash("An error occurred while updating the actual expense. Please try again later.", 'error')
            app.logger.error(f"Error updating budget expense: {str(e)}")
            return render_template('error.html', error_message='An error occurred')

    return redirect(url_for('track'))


@app.route('/delete_actual_income/<int:income_id>', methods=['POST', 'GET'])
@login_required
def delete_actual_income(income_id):
    actual_income = ActualIncome.query.get_or_404(income_id)

    # Check if the user trying to delete a budget income is the owner
    if actual_income.user_id != current_user.id:
        flash("You don't have permission to delete this data.", 'error')
        return render_template('error.html', error_message='Permission Denied')
    try:
        db.session.delete(actual_income)
        db.session.commit()
        flash('Actual Income Deleted Successfully', 'success')
        return redirect(url_for('track'))
    except SQLAlchemyError as e:
        db.session.rollback()
        flash("Failed to delete the actual income. Please try again later.", 'error')
        app.logger.error(f"Error deleting actual income: {str(e)}")
        return redirect(url_for('track'))


# Goldmine route
@app.route('/goldmine', methods=['GET', 'POST'])
@login_required
def goldmine():
    if "user_id" not in session:
        return redirect(url_for('login'))

    user_id = session["user_id"]
    curr_user = Users.query.get(user_id)

    try:
        # Query to get distinct years from BudgetedExpenses table
        budget_expenses_years = (
            db.session.query(BudgetedExpenses.year.distinct())
            .filter_by(user_id=user_id)
        )

        # Query to get distinct years from ActualIncome table
        actual_income_years = (
            db.session.query(extract('year', ActualIncome.date).distinct())
            .filter_by(user_id=user_id)
        )

        # Query to get distinct years from ActualExpenses table
        actual_expenses_years = (
            db.session.query(extract('year', ActualExpenses.date).distinct())
            .filter_by(user_id=user_id)
        )

        # Combine the results from all four queries using UNION
        years_in_db = (
            db.session.query(BudgetedIncome.year.distinct())
            .filter_by(user_id=user_id)
            .union(budget_expenses_years)
            .union(actual_income_years)
            .union(actual_expenses_years)
            .all()
        )

        # get the month request from form
        selected_month = request.args.get('month')

        # Get the Year from form
        selected_year = request.args.get('year')

        # Get the corresponding month number from the dictionary
        selected_month_number = month_name_to_number.get(selected_month)

        # get and calculate the total budget income
        total_budget_income = (db.session.query(func.sum(BudgetedIncome.budget_amount))
                               .filter_by(user_id=user_id, month_name=selected_month, year=selected_year)
                               .scalar())

        # get and calculate the total actual income
        total_actual_income = (db.session.query(func.sum(ActualIncome.actual_amount))
                               .filter_by(user_id=user_id)
                               .filter(extract('month', ActualIncome.date) == selected_month_number,
                                       extract('year', ActualIncome.date) == selected_year)
                               .scalar())

        # get and calculate the budget total expenses
        total_budget_expense = (db.session.query(func.sum(BudgetedExpenses.budget_amount))
                                .filter_by(user_id=user_id, month_name=selected_month, year=selected_year)
                                .scalar())

        # get and calculate total actual expenses
        total_actual_expense = (db.session.query(func.sum(ActualExpenses.actual_amount))
                                .filter_by(user_id=user_id)
                                .filter(extract('month', ActualExpenses.date) == selected_month_number,
                                        extract('year', ActualExpenses.date) == selected_year)
                                .scalar())

        # Query and calculate budget expenses by category which returns a list of tuples
        budget_expenses_by_category = (db.session.query(BudgetedExpenses.category_name,
                                                        func.sum(BudgetedExpenses.budget_amount))
                                       .filter_by(user_id=user_id, month_name=selected_month,
                                                  year=selected_year)
                                       .group_by(BudgetedExpenses.category_name).all())
        # Convert budget_expense_by_category list of tuples to separate lists for category name and budget amount
        budget_category_name_list = [item[0] for item in budget_expenses_by_category]
        budget_amount_list = [item[1] for item in budget_expenses_by_category]

        # Query and calculate total actual expenses by category which returns a list of tuples
        actual_expenses_by_category = (db.session.query(ActualExpenses.category_name,
                                                        func.sum(ActualExpenses.actual_amount))
                                       .filter_by(user_id=user_id)
                                       .filter(extract('month', ActualExpenses.date) == selected_month_number,
                                               extract('year', ActualExpenses.date) == selected_year)
                                       .group_by(ActualExpenses.category_name).all())
        # convert actual_expenses_by_category to separate lists for name and amount
        actual_category_name_list = [item[0] for item in actual_expenses_by_category]
        actual_amount_list = [item[1] for item in actual_expenses_by_category]

        # Earnings Sources
        # Budget Income
        budget_income_sources = (db.session.query(BudgetedIncome.income_name,
                                                  func.sum(BudgetedIncome.budget_amount))
                                 .filter_by(user_id=user_id, month_name=selected_month, year=selected_year)
                                 .group_by(BudgetedIncome.income_name).all())
        budget_income_sources_name = [item[0] for item in budget_income_sources]
        budget_income_sources_amount = [item[1] for item in budget_income_sources]

        # Actual Income
        actual_income_sources = (db.session.query(ActualIncome.income_name,
                                                  func.sum(ActualIncome.actual_amount))
                                 .filter_by(user_id=user_id)
                                 .filter(extract('month', ActualIncome.date) == selected_month_number,
                                         extract('year', ActualIncome.date) == selected_year)
                                 .group_by(ActualIncome.income_name).all())
        actual_income_sources_name = [item[0] for item in actual_income_sources]
        actual_income_sources_amount = [item[1] for item in actual_income_sources]

        # Total Actual Income and Expenses over time
        # Income
        income_over_time = (db.session.query(
            extract('month', ActualIncome.date).label('income_month'),
            func.sum(ActualIncome.actual_amount).label('total_income'))
                            .filter_by(user_id=user_id)
                            .filter(extract('year', ActualIncome.date) == selected_year)
                            .group_by('income_month')
                            .order_by('income_month')
                            .all()
                            )

        # Expense
        expense_over_time = (db.session.query(
            extract('month', ActualExpenses.date).label('expense_month'),
            func.sum(ActualExpenses.actual_amount).label('total_expense')
        )
                             .filter_by(user_id=user_id)
                             .filter(extract('year', ActualExpenses.date) == selected_year)
                             .group_by('expense_month')
                             .order_by('expense_month')
                             .all()
                             )
        # Calculate budget income coverage
        if total_actual_expense is None:
            total_actual_expense = 0
        if total_budget_expense is None:
            total_budget_expense = 0
        if total_actual_income is None:
            total_actual_income = 0
        if total_budget_income is None:
            total_budget_income = 0

            # to calculate the total budget income to expense ratio in percentage
        if total_budget_income is None or total_budget_income == 0:
            budget_income_coverage = 0
        elif total_budget_income >= total_budget_expense:
            budget_income_coverage = 100
        else:
            budget_income_coverage = round((total_budget_income / total_budget_expense) * 100, 2)

        # to calculate the total actual income to expense ratio in percentage
        if total_actual_expense is None or total_actual_expense == 0:
            actual_income_coverage = 0
        elif total_actual_income >= total_actual_expense:
            actual_income_coverage = 100
        else:
            actual_income_coverage = round((total_actual_income / total_actual_expense) * 100, 2)

        return render_template('goldmine.html', user=curr_user, selected_month=selected_month,
                               years_in_db=years_in_db, total_budget_income=total_budget_income,
                               selected_year=selected_year, total_actual_income=total_actual_income,
                               total_actual_expense=total_actual_expense, total_budget_expense=total_budget_expense,
                               budget_income_coverage=budget_income_coverage,
                               actual_income_coverage=actual_income_coverage,
                               budget_category_name_list=budget_category_name_list,
                               budget_amount_list=budget_amount_list,
                               actual_category_name_list=actual_category_name_list,
                               actual_amount_list=actual_amount_list,
                               budget_income_sources_name=budget_income_sources_name,
                               budget_income_sources_amount=budget_income_sources_amount,
                               actual_income_sources_name=actual_income_sources_name,
                               actual_income_sources_amount=actual_income_sources_amount,
                               income_over_time=income_over_time, expense_over_time=expense_over_time
                               )
    except Exception as e:
        app.logger.error(f"An error occurred in goldmine: {str(e)}")
        return render_template('error.html', error_message=f'{str(e)}')


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user_id = session["user_id"]
    curr_user = Users.query.get(user_id)

    if request.method == 'POST':
        # get form details
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')
        email = request.form.get('email')
        # Check if the username or email already exists in the database
        user_check = Users.query.filter(Users.username == username, Users.id != user_id).first()
        email_check = Users.query.filter(Users.email == email, Users.id != user_id).first()

        if user_check:
            flash('Username already exists', 'error')
        elif email_check:
            flash('Email already exists', 'error')
        else:
            # Update user information
            curr_user.username = username
            curr_user.firstname = firstname
            curr_user.lastname = lastname
            curr_user.email = email

            # Update password if provided
            if password:
                encrypted_password = generate_password_hash(password, method="sha256")
                curr_user.password = encrypted_password

            try:
                db.session.commit()
                flash("User Information Updated Successfully", 'success')
                return redirect(url_for('plan'))
            except Exception as e:
                db.session.rollback()
                flash("An error occurred while updating user information. Please try again later.", 'error')
                app.logger.error(f"Error updating user information: {str(e)}")

    return render_template('profile.html', user=curr_user)


@app.route('/delete_profile', methods=['GET', 'POST'])
@login_required
def delete_profile():
    if request.method == 'POST':
        # User has confirmed the deletion
        try:
            db.session.delete(current_user)
            db.session.commit()

            # Logout the user and clear their session
            logout_user()

            flash('Your profile has been deleted.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while deleting your profile. Please try again later.', 'error')
            app.logger.error(f"Error deleting user profile: {str(e)}")

    return redirect(url_for('delete_profile'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))
