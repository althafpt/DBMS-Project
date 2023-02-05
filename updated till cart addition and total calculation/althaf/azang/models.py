from azang import db, login_manager
from flask_login import UserMixin  #contains get_id,isauntheticated and other methods used to verify if the user has logged in or not
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


cart_product = db.Table('cart_product',
                        db.Column('cart_id', db.Integer, db.ForeignKey(
                            'cart.id'), primary_key=True),
                        db.Column('product_id', db.Integer, db.ForeignKey(
                            'product.id'), primary_key=True),
                        db.Column('user_id', db.Integer, db.ForeignKey(
                            'user.id'), primary_key=True),
                        )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(30),
                         nullable=False, unique=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'))
    cart = db.relationship('Cart', uselist=False,
                           back_populates='user', cascade='all, delete-orphan')
    products = db.relationship(
        'Product', back_populates='users')
    confirmed_orders = db.relationship(
        'ConfirmedOrders', back_populates='user')

    def __repr__(self):
        return f'User {self.user_name}'



    def check_password_correction(self,entered_password):  #this function is to check in our login page whether the password we entered in is correct or not
        if self.password==entered_password:
            return True
        else: 
            return False


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    product_name=db.Column(db.String, nullable=False)
    product_price=db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='cart')
    def __repr__(self):
        return f'product {self.id}'
    

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(1024), unique=True)
    users = db.relationship(
        'User', secondary='cart_product', back_populates='products')
    confirmed_orders = db.relationship(
        'ConfirmedOrders', back_populates='product')
    def __repr__(self):
        return f'Product {self.name}'


class ConfirmedOrders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    user = db.relationship('User', back_populates='confirmed_orders')
    product = db.relationship('Product', back_populates='confirmed_orders')
