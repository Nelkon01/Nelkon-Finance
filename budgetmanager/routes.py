from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from budgetmanager import app, db
from budgetmanager.models import Users, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses


# Home route
@app.route('/')
def home():
    if "user_id" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)
        return render_template('plan.html', user=curr_user)
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
    if not current_user.is_authenticated:
        flash('Please log in to access your account', 'error')
    else:
        return redirect(url_for('home'))

    if request.method == 'POST':
        session.permanent = True
        username = request.form['username']
        password = request.form['password']

        if not username or not password:  # Check for empty fields
            flash('Please enter both username and password', 'error')
            return redirect(url_for('login'))

        curr_user = Users.query.filter_by(username=username).first()
        if curr_user and check_password_hash(curr_user.password, password):
            login_user(curr_user)  # Login the user in
            flash('Logged in successfully!', 'success')
            session["user_id"] = curr_user.id
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route('/add_budget_expense', methods=['POST', 'GET'])
def add_budget_expense():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    #     collect form data from add_budget_expense form
    month_name = request.form.get('month_name')
    category_name = request.form.get('category_name')
    budget_amount = request.form.get('budget_amount')

    budgeted_expense = BudgetedExpenses(
        category_name=category_name,
        user_id=current_user.id,
        month_name=month_name,
        budget_amount=budget_amount
    )
    db.session.add(budgeted_expense)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_budget_income', methods=['POST', 'GET'])
def add_budget_income():
    #     collect form data from add_budget_expense form
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    month_name = request.form.get('month_name')
    income_name = request.form.get('income_name')
    budget_amount = request.form.get('budget_amount')

    budgeted_income = BudgetedIncome(
        income_name=income_name,
        user_id=current_user.id,
        month_name=month_name,
        budget_amount=budget_amount
    )
    db.session.add(budgeted_income)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_actual_expense', methods=['POST', 'GET'])
def add_actual_expense():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    #     collect form data from add_actual_expense form
    date = request.form.get('date')
    expense_name = request.form.get('expense_name')
    category_name = request.form.get('category_name')
    actual_amount = request.form.get('actual_amount')

    actual_expense = ActualExpenses(
        category_name=category_name,
        user_id=current_user.id,
        date=date,
        actual_amount=actual_amount,
        expense_name=expense_name
    )
    db.session.add(actual_expense)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_actual_income', methods=['POST', 'GET'])
def add_actual_income():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    #     collect form data from add_actual_expense form
    date = request.form.get('date')
    income_name = request.form.get('income_name')
    actual_amount = request.form.get('actual_amount')

    actual_income = ActualIncome(
        income_name=income_name,
        user_id=current_user.id,
        date=date,
        actual_amount=actual_amount,
    )
    db.session.add(actual_income)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))
