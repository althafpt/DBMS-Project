from flask import Flask,render_template,current_app,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///azang.db'
app.config['SECRET_KEY']='46f0db5f44d8553510500c94' 
app.app_context().push()
db = SQLAlchemy(app)

bcrypt=Bcrypt(app) #this is used to in order to save passwords in the database as hashed values instead of text passwords for security purposes
login_manager = LoginManager(app) #instance for login built in function
login_manager.login_view="loginpage" #this is used so that if the user is not logged in then they are redirected to the login page in order to view the market 
login_manager.login_message_category="info"

from azang import routes