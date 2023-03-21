from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/user_authentication_db'