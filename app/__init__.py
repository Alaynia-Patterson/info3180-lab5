from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config
from flask_wtf.csrf import CSRFProtect  # Import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)

# Initialize CSRF protection
csrf = CSRFProtect(app)

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db) 


from app import views
from app import models  # Important for migrations