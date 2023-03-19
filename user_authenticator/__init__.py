from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from user_authenticator.config import ApplicationConfig

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
db = SQLAlchemy(app)

from user_authenticator import views