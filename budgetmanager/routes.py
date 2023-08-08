from flask import render_template, request, redirect, url_for
from budgetmanager import app, db
from budgetmanager.models import Users, Month, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses, Category


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/categories', methods=['GET'])
def categories():
    categories = ['Shopping', 'Groceries', 'Eating Out', 'Transport', 'Bills', 'Entertainment', 'Miscellaneous']

    for category_name in categories:
        category = Category(name=category_name)
        db.session.add(category)

    db.session.commit()
    return "Categories added to database"
