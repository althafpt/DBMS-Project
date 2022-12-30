from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')