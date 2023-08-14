from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_user
from werkzeug.security import check_password_hash

from budgetmanager import app, db
from budgetmanager.models import Users, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses


@app.route('/')
def home():
    return render_template('plan.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = Users.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)  # Login the user in
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        print(request.form)
        users = Users(
            username=request.form.get("username"),
            firstname=request.form.get("firstname"),
            lastname=request.form.get("lastname"),
            password=request.form.get("password"),
            email=request.form.get("email")
        )
        print(users)
        db.session.add(users)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        return render_template("signup.html")


@app.route("/user")
def user():
    if "users" in session:
        users = session.get("users.username")
        return f"{users}"
    else:
        return render_template("signup.html")


@app.route('/add_budget_expense', methods=['POST', 'GET'])
def add_budget_expense():
    #     collect form data from add_budget_expense form
    month_name = request.form.get('month_name')
    category_name = request.form.get('category_name')
    budget_amount = request.form.get('budget_amount')

    budgeted_expense = BudgetedExpenses(
        category_name=category_name,
        user_id=user.user_id,
        month_name=month_name,
        budget_amount=budget_amount
    )
    db.session.add(budgeted_expense)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_budget_income', methods=['POST', 'GET'])
def add_budget_income():
    #     collect form data from add_budget_expense form
    month_name = request.form.get('month_name')
    income_name = request.form.get('income_name')
    budget_amount = request.form.get('budget_amount')

    budgeted_income = BudgetedExpenses(
        income_name=income_name,
        user_id=user.user_id,
        month_name=month_name,
        budget_amount=budget_amount
    )
    db.session.add(budgeted_income)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_actual_expense', methods=['POST', 'GET'])
def add_actual_expense():
    #     collect form data from add_actual_expense form
    date = request.form.get('date')
    expense_name = request.form.get('expense_name')
    category_name = request.form.get('category_name')
    actual_amount = request.form.get('actual_amount')

    actual_expense = ActualExpenses(
        category_name=category_name,
        user_id=user.user_id,
        date=date,
        actual_amount=actual_amount,
        expense_name=expense_name
    )
    db.session.add(actual_expense)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_actual_income', methods=['POST', 'GET'])
def add_actual_income():
    #     collect form data from add_actual_expense form
    date = request.form.get('date')
    income_name = request.form.get('income_name')
    actual_amount = request.form.get('actual_amount')

    actual_income = ActualIncome(
        income_name=income_name,
        user_id=user.user_id,
        date=date,
        actual_amount=actual_amount,
    )
    db.session.add(actual_income)
    db.session.commit()
    return redirect(url_for('home'))
