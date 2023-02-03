from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #config dictionary accepts values from us and used URI not URL for the identifier 
app.config['SECRET_KEY']='d887994e1cefece410b3a881' #secret key for forms
app.app_context().push() # to avoid the db.create_all() error
db = SQLAlchemy(app)
bcrypt=Bcrypt(app) #this is used to in order to save passwords in the database as hashed values instead of text passwords for security purposes
login_manager = LoginManager(app) #instance for login built in function
login_manager.login_view="loginpage" #this is used so that if the user is not logged in then they are redirected to the login page in order to view the market 
login_manager.login_message_category="info"

from market import routes