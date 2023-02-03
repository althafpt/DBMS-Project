from flask import Flask,render_template,url_for,redirect,request
app = Flask(__name__)

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