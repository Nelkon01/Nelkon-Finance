import os  # Module that enables interaction with operating system
from datetime import timedelta

from flask import Flask  # Framework to build python webapps
from flask_sqlalchemy import SQLAlchemy  # ORM to interact with database
from flask_login import LoginManager  # Import LoginManager

# check if env.py exists which would store environment variables like
# db credentials
if os.path.exists('env.py'):
    import env

# create a flask app
app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
    app.permanent_session_lifetime = timedelta(minutes=15)
else:
    uri = os.environ.get("DB_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

# Initialise LoginManager
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from .models import Users  # Import the Users class
    return Users.query.get(int(user_id))


from budgetmanager import routes  # noqa
