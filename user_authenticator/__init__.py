from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from user_authenticator.config import ApplicationConfig

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from user_authenticator.models import User

with app.app_context():
    db.create_all()

from user_authenticator import views