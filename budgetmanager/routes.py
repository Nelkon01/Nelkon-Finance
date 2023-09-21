import json
from datetime import datetime

from flask import render_template, request, redirect, url_for, session, flash, jsonify, abort
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import func, extract

from budgetmanager import app, db
from budgetmanager.models import Users, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses


# Home route
@app.route('/')
def home():
    if "user_id" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)

        # Filter budget incomes and expenses by user ID
        budget_incomes = BudgetedIncome.query.filter_by(user_id=user_id).order_by(BudgetedIncome.month_name).all()
        budget_expenses = BudgetedExpenses.query.filter_by(user_id=user_id).order_by(BudgetedExpenses.month_name).all()

        return render_template('plan.html', user=curr_user, budget_incomes=budget_incomes,
                               budget_expenses=budget_expenses)
    else:
        return redirect(url_for("login"))


@app.route('/track')
def track():
    if "user_id" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)

        # query and filter the actual incomes and expenses
        actual_incomes = ActualIncome.query.filter_by(user_id=user_id).order_by(ActualIncome.date).all()
        actual_expenses = ActualExpenses.query.filter_by(user_id=user_id).order_by(ActualExpenses.date).all()

        return render_template('track.html', user=curr_user, actual_incomes=actual_incomes,
                               actual_expenses=actual_expenses)
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

        user_check = Users.query.filter_by(username=username).first()
        email_check = Users.query.filter_by(email=email).first()

        if user_check:
            flash('Username already exists', 'error')
            return redirect(url_for('signup'))
        elif email_check:
            flash('Email already exists', 'error')
            return redirect(url_for('signup'))
        else:
            encrypted_password = generate_password_hash(password, method="sha256")
            new_user = Users(username=username, firstname=firstname, lastname=lastname, password=encrypted_password,
                             email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', 'success')
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        identifier = request.form['identifier']
        password = request.form['password']

        if not identifier or not password:
            flash('Please enter both username/email and password', 'error')
            return redirect(url_for('login'))

        curr_user = Users.query.filter(
            (Users.username == identifier) | (Users.email == identifier)
        ).first()
        if curr_user and check_password_hash(curr_user.password, password):
            login_user(curr_user)
            flash('Logged in successfully!', 'success')
            session.permanent = True
            session["user_id"] = curr_user.id
            return redirect(url_for('home'))
        else:
            flash('Invalid username/email or password', 'error')

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    flash('Please login to access your account', 'error')
    return render_template('login.html')


@app.route('/add_budget_income', methods=['POST', 'GET'])
def add_budget_income():
    # Validate user
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    #     collect form data from add_budget_expense form
    month_name = request.form.get('month_name')
    year = request.form.get('year')
    income_name = request.form.get('income_name')
    budget_amount = request.form.get('budget_amount')

    budgeted_income = BudgetedIncome(
        income_name=income_name,
        user_id=session["user_id"],
        month_name=month_name,
        year=year,
        budget_amount=budget_amount
    )
    db.session.add(budgeted_income)
    db.session.commit()
    return redirect(url_for('home'))


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


@app.route('/edit_budget_income/<int:income_id>', methods=['POST', 'GET'])
def edit_budget_income(income_id):
    # Validate user
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    # Get the budget income record by income id
    budget_income = BudgetedIncome.query.get_or_404(income_id)
    if request.method == 'POST':
        #     collect form data from add_budget_expense form
        month_name = request.form.get('month_name')
        income_name = request.form.get('income_name')
        budget_amount = request.form.get('budget_amount')

        # update the budget income values of that id
        budget_income.month_name = month_name
        budget_income.income_name = income_name
        budget_income.budget_amount = budget_amount

        db.session.commit()
        flash("Budget Income updated Successfully", 'success')
    return redirect(url_for('home'))


@app.route('/delete_budget_income/<int:income_id>', methods=['POST', 'GET'])
def delete_budget_income(income_id):
    #     Validate user
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    budget_income = BudgetedIncome.query.get_or_404(income_id)
    db.session.delete(budget_income)
    db.session.commit()
    flash('Budget Income Deleted Successfully', 'success')
    return redirect(url_for('home'))


@app.route('/add_budget_expense', methods=['POST', 'GET'])
def add_budget_expense():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    #     collect form data from add_budget_expense form
    month_name = request.form.get('month_name')
    year = request.form.get('year')
    category_name = request.form.get('category_name')
    budget_amount = request.form.get('budget_amount')

    budgeted_expense = BudgetedExpenses(
        category_name=category_name,
        user_id=session["user_id"],
        month_name=month_name,
        year=year,
        budget_amount=budget_amount
    )
    db.session.add(budgeted_expense)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/edit_budget_expense/<int:expense_id>', methods=['POST', 'GET'])
def edit_budget_expense(expense_id):
    # Validate User
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    #     Get budget expenses by id
    budget_expenses = BudgetedExpenses.query.get_or_404(expense_id)
    if request.method == 'POST':
        #   Collect form data from form
        month_name = request.form.get('month_name')
        category_name = request.form.get('category_name')
        budget_amount = request.form.get('budget_amount')

        #   update the budget expense values
        budget_expenses.month_name = month_name
        budget_expenses.category_name = category_name
        budget_expenses.budget_amount = budget_amount

        db.session.commit()
        flash("Budget Expense updated Successfully", 'success')
    return redirect(url_for('home'))


@app.route('/delete_budget_expense/<int:expense_id>', methods=['POST', 'GET'])
def delete_budget_expense(expense_id):
    #    user validation
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    budget_expense = BudgetedExpenses.query.get_or_404(expense_id)
    db.session.delete(budget_expense)
    db.session.commit()
    flash('Budget Expense Deleted Successfully', 'success')
    return redirect(url_for('home'))


@app.route('/add_actual_expense', methods=['POST', 'GET'])
def add_actual_expense():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    #     collect form data from add_actual_expense form
    date_str = request.form.get('date')
    expense_name = request.form.get('expense_name')
    category_name = request.form.get('category_name')
    actual_amount = request.form.get('actual_amount')

    date = datetime.strptime(date_str, "%d/%m/%Y")
    actual_expense = ActualExpenses(
        category_name=category_name,
        user_id=session["user_id"],
        date=date,
        actual_amount=actual_amount,
        expense_name=expense_name
    )
    db.session.add(actual_expense)
    db.session.commit()
    return redirect(url_for('track'))


@app.route('/edit_actual_expense/<int:expense_id>', methods=['POST', 'GET'])
def edit_actual_expense(expense_id):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    #   Get Actual Expenses by ID
    actual_expense = ActualExpenses.query.get_or_404(expense_id)
    if request.method == 'POST':
        #   collect data from form
        date = request.form.get('date')
        expense_name = request.form.get('expense_name')
        category_name = request.form.get('category_name')
        actual_amount = request.form.get('actual_amount')

        #         update values
        actual_expense.date = date
        actual_expense.expense_name = expense_name
        actual_expense.category_name = category_name
        actual_expense.actual_amount = actual_amount

        db.session.commit()
        flash('Actual Expense Updated Successfully', 'success')
    return redirect(url_for('track'))


@app.route('/delete_actual_expense/<int:expense_id>', methods=['POST', 'GET'])
def delete_actual_expense(expense_id):
    if not current_user.is_authenticated:
        redirect(url_for('login'))

    actual_expense = ActualExpenses.query.get_or_404(expense_id)
    db.session.delete(actual_expense)
    db.session.commit()
    flash('Actual Expense Deleted Successfully', 'success')
    return redirect(url_for('track'))


# Add Actual Income route
@app.route('/add_actual_income', methods=['POST', 'GET'])
def add_actual_income():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    #     collect form data from add_actual_expense form
    date_str = request.form.get('date')
    income_name = request.form.get('income_name')
    actual_amount = request.form.get('actual_amount')

    date = datetime.strptime(date_str, "%d/%m/%Y")
    month_string = date.strftime('%B')
    actual_income = ActualIncome(
        income_name=income_name,
        user_id=session["user_id"],
        date=date,
        actual_amount=actual_amount,
    )
    db.session.add(actual_income)
    db.session.commit()
    return redirect(url_for('track'))


@app.route('/edit_actual_income/<int:income_id>', methods=['POST', 'GET'])
def edit_actual_income(income_id):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    #   Get Actual Income by ID
    actual_income = ActualIncome.query.get_or_404(income_id)
    if request.method == 'POST':
        #   collect data from form
        date = request.form.get('date')
        income_name = request.form.get('income_name')
        actual_amount = request.form.get('actual_amount')

        #         update values
        actual_income.date = date
        actual_income.income_name = income_name
        actual_income.actual_amount = actual_amount

        db.session.commit()
        flash('Actual Expense Updated Successfully', 'success')
    return redirect(url_for('track'))


@app.route('/delete_actual_income/<int:income_id>', methods=['POST', 'GET'])
def delete_actual_income(income_id):
    if not current_user.is_authenticated:
        redirect(url_for('login'))

    actual_income = ActualIncome.query.get_or_404(income_id)
    db.session.delete(actual_income)
    db.session.commit()
    flash('Actual Income Deleted Successfully', 'success')
    return redirect(url_for('track'))


# Goldmine route
@app.route('/goldmine', methods=['GET', 'POST'])
def goldmine():
    if "user_id" not in session:
        return redirect(url_for('login'))

    user_id = session["user_id"]
    curr_user = Users.query.get(user_id)

    try:
        years_in_db = (db.session.query(extract('year', ActualIncome.date).distinct())
                       .filter_by(user_id=user_id).all())

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
        abort(500)


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
            if password:
                encrypted_password = generate_password_hash(password, method="sha256")
                curr_user.password = encrypted_password
            curr_user.username = username
            curr_user.firstname = firstname
            curr_user.lastname = lastname
            curr_user.email = email

        db.session.commit()
        flash("User Information Updated Successfully", 'success')
        return redirect(url_for('home'))

    return render_template('profile.html', user=curr_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))
