from budgetmanager import db


class Users(db.Model):
    # schema for users table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        # __repr__ method for Users class to return a string representation of the object
        return f"User('{self.username}', '{self.firstname}', '{self.lastname}', '{self.email}')"
    

class Month(db.Model):
    # schema for month table
    month_id = db.Column(db.Integer, primary_key=True)
    month_name = db.Column(db.String(20), nullable=False, unique=True)
    
    def __repr__(self):
        # __repr__ method for Month class to return a string representation of the object
        return f"Month('{self.month_name}')"
    

class BudgetedIncome(db.Model):
    # schema for budgeted income table
    income_id = db.Column(db.Integer, primary_key=True)
    income_name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    month_id = db.Column(db.Integer, db.ForeignKey('month.month_id'), nullable=False)