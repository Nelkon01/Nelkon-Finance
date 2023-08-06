import os  # Module that enables interaction with operating system
from flask import Flask  # Framework to build python webapps
from flask_sqlalchemy import SQLAlchemy  # library that allows pytHon work with db

# check if env.py exists which would store environment variables like
# db credentials
if os.path.exists('env.py'):
    import env

# create a flask app
app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

from budgetmanager import routes # noqa
