from flask import render_template, request, redirect, url_for, session
from budgetmanager import app, db
from budgetmanager.models import Users, Month, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses, Category


@app.route('/')
def home():
    categories = Category.query.all()
    return render_template('plan.html')


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


@app.route('/categories', methods=['GET', 'POST'])
def categories():
    spending_categories = ['Shopping', 'Groceries', 'Eating Out', 'Transport', 'Bills', 'Entertainment',
                           'Miscellaneous']
    for category_name in spending_categories:
        category = Category(category_name=category_name)
        db.session.add(category)

    db.session.commit()
    return "Categories added to database"


@app.route('/add_budget_expense', methods=['POST', 'GET'])
def add_budget_expense():
    #     collect form data from add_budget_expense form
    month_id = request.form.get('month_name')
    category_name = request.form.get('category_name')
    budget_amount = request.form.get('budget_amount')

    # category = Category.query.filter_by(category_name=category_name).first()
    user_id = 1

    budgeted_expense = BudgetedExpenses(
        category_name=category_name,
        user_id=user_id,
        month_id=month_id,
        budget_amount=budget_amount
    )
    db.session.add(budgeted_expense)
    db.session.commit()
    return redirect(url_for('home'))
