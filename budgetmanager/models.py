from budgetmanager import db


class Users(db.Model):
    # schema for users table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    budgeted_incomes = db.relationship("BudgetedIncome", backref="user", cascade="all, delete", lazy=True)
    actual_incomes = db.relationship("ActualIncome", backref="user", cascade="all, delete", lazy=True)
    budgeted_expenses = db.relationship("BudgetedExpenses", backref="user", cascade="all, delete", lazy=True)
    actual_expenses = db.relationship("ActualExpenses", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ method for Users class to return a string representation of the object
        return f"#:{self.id} -  Username: {self.username} - Firstname: {self.firstname} - Lastname: {self.lastname} - Password: {self.password} - Email: {self.email}"


USER_ID = 'users.id'


class BudgetedIncome(db.Model):
    # schema for budgeted income table
    income_id = db.Column(db.Integer, primary_key=True)
    income_name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(USER_ID, ondelete="cascade"), nullable=False)
    month_name = db.Column(db.String(20), nullable=False)
    budget_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        # __repr__ method for BudgetedIncome class to return a string representation of the object
        return f"BudgetedIncome('{self.income_name}', '{self.user_id}', '{self.month_name}', '{self.budget_amount}')"


class ActualIncome(db.Model):
    # schema for actual income table
    income_id = db.Column(db.Integer, primary_key=True)
    income_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(USER_ID, ondelete="cascade"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    actual_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        # __repr__ method for ActualIncome class to return a string representation of the object
        return f"ActualIncome('{self.income_name}', '{self.user_id}', '{self.date}' '{self.actual_amount}')"


class BudgetedExpenses(db.Model):
    # schema for budgeted expenses table
    expense_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(USER_ID, ondelete="cascade"), nullable=False)
    month_name = db.Column(db.String(20), nullable=False)
    budget_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        # __repr__ method for BudgetedExpenses class to return a string representation of the object
        return f"BudgetedExpenses('{self.category_name}', '{self.user_id}', '{self.month_name}, '{self.budget_amount}')"


class ActualExpenses(db.Model):
    # schema for actual expenses table
    expense_id = db.Column(db.Integer, primary_key=True)
    expense_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(USER_ID, ondelete="cascade"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    category_name = db.Column(db.String(20), nullable=False)
    actual_amount = db.Column(db.Float, nullable=False)

    def __repr__(self):
        # __repr__ method for ActualExpenses class to return a string representation of the object
        return (f"ActualExpenses('{self.expense_name}', '{self.user_id}', '{self.date}', '{self.category_name}',"
                f" '{self.actual_amount}')")
