from azang import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False, unique=True)
    cart = db.relationship('Cart', uselist=False,back_populates='user', cascade='all, delete-orphan')
    products = db.relationship('Product', secondary='cart_product', back_populates='users')
    confirmed_orders = db.relationship('ConfirmedOrder', back_populates='user')

    def __repr__(self):
        return f'User {self.user_name}'

cart_product = db.Table('cart_product',db.Column('cart_id', db.Integer, db.ForeignKey('cart.id'), primary_key=True),db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True))


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    qty = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='cart')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    users = db.relationship(
                            'User', secondary='cart_product', back_populates='products'
                           )
    confirmed_orders = db.relationship(
                                        'ConfirmedOrder', back_populates='product'
                                    )

    def __repr__(self):
        return f'Product {self.name}'

class ConfirmedOrders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(
        db.Integer, db.ForeignKey('product.id'), nullable=False
                            )
    user = db.relationship('User', back_populates='confirmed_orders')
    product = db.relationship('Product', back_populates='confirmed_orders')