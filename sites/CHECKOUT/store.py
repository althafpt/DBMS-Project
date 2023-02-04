from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///checkout.db'
db = SQLAlchemy(app)

class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120))
    address = db.Column(db.String(200))
    card_number = db.Column(db.String(16))
    expiration_date = db.Column(db.String(5))
    cvv = db.Column(db.String(3))

    def __repr__(self):
        return '<Checkout %r>' % self.name

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        checkout = Checkout(name=request.form['name'], email=request.form['email'], address=request.form['address'], card_number=request.form['card-number'], expiration_date=request.form['expiration-date'], cvv=request.form['cvv'])
        db.session.add(checkout)
        db.session.commit()
        return 'Checkout successful!'
    return render_template('checkout.html')