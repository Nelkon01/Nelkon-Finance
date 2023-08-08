from flask import render_template, request, redirect, url_for
from budgetmanager import app, db
from budgetmanager.models import Users, Month, BudgetedIncome, ActualIncome, BudgetedExpenses, ActualExpenses


@app.route('/')
def home():
    return render_template('home.html')
