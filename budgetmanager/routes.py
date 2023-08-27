from datetime import datetime

from flask import render_template, request, redirect, url_for, session, flash, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from dash import Dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from sqlalchemy import and_

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


@app.route('/goldmine')
def goldmine():
    if "user_id" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)
        return render_template('goldmine.html', user=curr_user)
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


# Define dash layout
dash_app = Dash(__name__, server=app, url_base_pathname='/dashboard/')
dash_app.layout = html.Div([
    html.H1("See your Goldmine"),
    html.Div(id='user-greeting'),

    # Card for displaying total income
    html.Div([
        html.Div([
            html.H3("Total Income for the selected Month"),
            html.P("Select Month: "),
            dcc.Dropdown(
                id='month-dropdown',
                options=[
                    {'label': 'January', 'value': 'January'},
                    {'label': 'February', 'value': 'February'},
                    {'label': 'March', 'value': 'March'},
                    {'label': 'April', 'value': 'April'},
                    {'label': 'May', 'value': 'May'},
                    {'label': 'June', 'value': 'June'},
                    {'label': 'July', 'value': 'July'},
                    {'label': 'August', 'value': 'August'},
                    {'label': 'September', 'value': 'September'},
                    {'label': 'October', 'value': 'October'},
                    {'label': 'November', 'value': 'November'},
                    {'label': 'December', 'value': 'December'},
                ],
                value='January',
            ),
        ]),
        # Total Income Card Placeholder
        # html.Div(id='total-income-card'),
    ], className='card'),

    # Placeholder for other graphs
    dcc.Graph(id='example-graph'),

])


@dash_app.callback(Output('user-greeting', 'children'), [Input('/', '/')])
def update_user_greeting(pathname):
    if current_user.is_authenticated:
        return html.P(f"Hello, {current_user.username}!")
    else:
        return html.P("You are not logged in.")


@app.route('/calculate_total_budget_income', methods=['POST'])
@login_required
def calculate_total_budget_income():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    month_name = request.json.get('month_name')
    if not month_name:
        return jsonify({'error': 'Month name is required'})

    user_id = current_user.id
    total_budget_income = 0

    budgeted_incomes = BudgetedIncome.query.filter_by(user_id=user_id, month_name=month_name).all()

    for income in budgeted_incomes:
        total_budget_income += income.budget_amount

    return jsonify({'total_budget_income': total_budget_income})


@app.route('/calculate_total_actual_income', methods=['POST'])
@login_required
def calculate_total_actual_income():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    month_name = request.json.get('month_name')
    if not month_name:
        return jsonify({'error': 'Month name is required'})

    user_id = current_user.id
    total_actual_income = 0

    # Convert month name to month number
    month_number = datetime.datetime.strptime(month_name, '%B').month

    actual_incomes = ActualIncome.query.filter(
        and_(ActualIncome.user_id == user_id, ActualIncome.date.month == month_number)
    ).all()

    for income in actual_incomes:
        total_actual_income += income.actual_amount

    return jsonify({'total_actual_income': total_actual_income})


@dash_app.callback(Output('total-income-card', 'children'), Input('month-dropdown', 'value'))
def update_total_income_card(selected_month):
    # Calculate total income for the selected month and user
    total_income = calculate_total_budget_income(session["user_id"], selected_month)

    #     create card content
    card_content = html.Div([
        html.h4(f"Total Income for {selected_month}"),
        html.P(f"${total_income}"),
    ])
    return card_content
