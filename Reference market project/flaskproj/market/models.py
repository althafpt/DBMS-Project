from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin  #contains get_id,isauntheticated and other methods used to verify if the user has logged in or not
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin): 
    id=db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=20),nullable=False)
    amount=db.Column(db.Integer(),nullable=False,default=1000)
    
    items = db.relationship('Item',backref='owned_user',lazy=True) #lazy is used in order for sqlalchemy to fetch all the fields in a single fetch

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self,entered_password):  #this function is to check in our login page whether the password we entered in is correct or not
        if bcrypt.check_password_hash(self.password_hash, entered_password):
            return True
        else: 
            return False

    def can_purchase(self,item_obj):
        return self.amount >= item_obj.price
    
    def can_sell(self,item_obj):
        return self.id == item_obj.owner



class Item(db.Model):  # capital M for 'M'odel is important
    id=db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30),nullable=False)
    price=db.Column(db.Integer(),nullable=False)
    barcode=db.Column(db.String(length=15),unique=True)
    description = db.Column(db.String(length=1000),nullable=False)

    owner=db.Column(db.Integer,db.ForeignKey('user.id'))
    def __repr__(self):
        return f'item id : {self.id} item name : {self.name}' #this gives the name and id of the product when we give query.all()

    def buy(self,user):
                self.owner=user.id
                user.amount -= self.price
                db.session.commit()
    
    def sell(self,user):
        self.owner=None
        user.amount += self.price
        db.session.commit()
