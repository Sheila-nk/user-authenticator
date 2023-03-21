from sqlalchemy import MetaData
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from user_authenticator.config import ApplicationConfig

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
db = SQLAlchemy(app, metadata=metadata)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db, render_as_batch=True)

from user_authenticator import views