from flask import Flask

app = Flask(__name__)

from user_authenticator import views