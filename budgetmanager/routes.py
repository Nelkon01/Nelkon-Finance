from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from budgetmanager import app, db
from budgetmanager.models import Users, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses


@app.route('/')
def home():
    if "user" in session:
        user_id = session["user_id"]
        curr_user = Users.query.get(user_id)
        return render_template('plan.html', user=curr_user)
    else:
        return redirect(url_for("login"))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        encrypted_password = generate_password_hash(request.form.get("password"), method="sha256")
        users = Users(
            username=request.form.get("username"),
            firstname=request.form.get("firstname"),
            lastname=request.form.get("lastname"),
            password=encrypted_password,
            email=request.form.get("email")
        )
        db.session.add(users)
        db.session.commit()
        return redirect(url_for("login"))
    else:
        return render_template("signup.html")


@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    password = request.form.get('password')
    email = request.form.get('email')

    user_check = Users.query.filter_by(username=username).first()
    email_check = Users.query.filter_by(email=email).first()
    if user_check:
        flash('Username already exists', 'error')
        return redirect(url_for('signup'))
    elif email_check:
        flash('Email already exists', 'error')
        return redirect(url_for('signup'))
    else:
        new_user = Users(username=username, firstname=firstname, lastname=lastname, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.permanent = True
        username = request.form['username']
        password = request.form['password']

        curr_user = Users.query.filter_by(username=username).first()
        if curr_user and check_password_hash(curr_user.password, password):
            login_user(curr_user)  # Login the user in
            flash('Logged in successfully!', 'success')
            session["user_id"] = curr_user.id
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route("/user")
def user():
    if "users" in session:
        users = session.get("users.username")
        return f"{users}"
    else:
        return render_template("signup.html")


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
