import datetime
from uuid import uuid4

from user_authenticator import app, db, bcrypt

def get_uuid():
    return uuid4().hex

class User(db.Model):
    """User model for storing user information"""
    __tablename__ = "users"

    id = db.Column(db.String(32), unique=True, primary_key=True, nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(345), unique=True, nullable=False)
    password = db.Column(db.String(72), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, firstname, lastname, email, password):
        self.id = get_uuid()
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.registered_on = datetime.datetime.now()
        
    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}', '{self.registered_on}')"
