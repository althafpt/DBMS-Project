from flask import Flask,render_template,current_app,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///azang.db'
app.app_context().push()
db = SQLAlchemy(app)

from azang import routes