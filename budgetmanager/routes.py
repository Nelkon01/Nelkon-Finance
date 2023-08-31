from datetime import datetime

from flask import render_template, request, redirect, url_for, session, flash, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import func

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


@app.route('/track')
def track():
    if "user_id" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)
        return render_template('track.html', user=curr_user)
    else:
        return redirect(url_for("login"))


@app.route('/goldmine', methods=['GET', 'POST'])
def goldmine():
    if "user_id" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)

        # get the month request from form
        selected_month = request.args.get('month')

        # get and calculate the total budget income
        total_budget_income = (db.session.query(func.sum(BudgetedIncome.budget_amount))
                               .filter_by(user_id=user_id, month_name=selected_month).scalar())
        return render_template('goldmine.html', user=curr_user, selected_month=selected_month,
                               total_budget_income=total_budget_income)
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
        user_id=session["user_id"],
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
        user_id=session["user_id"],
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


@app.route('/add_actual_income', methods=['POST', 'GET'])
def add_actual_income():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    #     collect form data from add_actual_expense form
    date_str = request.form.get('date')
    income_name = request.form.get('income_name')
    actual_amount = request.form.get('actual_amount')

    date = datetime.strptime(date_str, "%d/%m/%Y")
    actual_income = ActualIncome(
        income_name=income_name,
        user_id=session["user_id"],
        date=date,
        actual_amount=actual_amount,
    )
    db.session.add(actual_income)
    db.session.commit()
    return redirect(url_for('track'))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))
