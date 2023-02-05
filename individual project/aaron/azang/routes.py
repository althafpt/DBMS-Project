from azang import app,db
from flask import render_template,redirect,url_for,request
from azang.models import User,Product
@app.route('/')
@app.route('/home')
def home():
    if request.method == "GET":
        items=Product.query.all()
        
        return render_template('home.html',items=items)

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