import os  # Module that enables interaction with operating system
from flask import Flask  # Framework to build python webapps
from flask_sqlalchemy import SQLAlchemy  # ORM to interact with database
from flask_login import LoginManager  # Import LoginManager
from .models import Users # Import the Users class

# check if env.py exists which would store environment variables like
# db credentials
if os.path.exists('env.py'):
    import env

# create a flask app
app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

# Initialise LoginManager
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


from budgetmanager import routes  # noqa
