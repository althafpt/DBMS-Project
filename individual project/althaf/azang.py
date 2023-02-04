from flask import Flask,render_template,current_app,url_for,redirect,request
from flask_sqlalchemy import SQLAlchemy
app = Flask( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///azang.db'
app.app_context().push()
db = SQLAlchemy(app)
class Item(db.Model):
    pid = db.Column(db.Integer(),primary_key=True)
    pname = db.Column(db.String(length=30), nullable=False)
    pprice = db.Column(db.Integer(),nullable=False)
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/reg')
def reg():
    return render_template('reg.html')
@app.route('/checkout')  
def checkout():
    return render_template('checkout.html')