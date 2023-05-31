from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models User, Role
from flask_login import LoginManager, login_manager, login_user
from flask_security import Security, SQLAlchemySessionUserDatastore
from flask import render_template, redirect, url_for

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lavie@localhost:5432/flask_rback'
app.config['SECRET_KEY'] = 'MY_SECRET'
app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False

db = SQLAlchemy()
db.init_app(app)

app.app_context().push()

@app.before_first_request
def create_tables():
    db.create_all()


user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)


@app.route('/')
def index():
    return render_template("index.html")