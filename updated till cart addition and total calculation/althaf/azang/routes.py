from azang import app,db
from flask import render_template,redirect,url_for,request,flash,get_flashed_messages
from azang.models import User,Product,Cart,ConfirmedOrders
from azang.forms import RegisterForm,LoginForm,addtocartForm,checkoutform
from flask_login import login_user, logout_user, login_required, current_user
import random
@app.route('/')
@app.route('/home',methods=['POST','GET'])
def home():
    form = addtocartForm()
    items=Product.query.all()
    if request.method == "POST":
        item_in_cart = request.form.get('item_in_cart')
        p_item_object = Product.query.filter_by(name=item_in_cart).first()
        if p_item_object:
                    itemtocart = Cart( user_id=current_user.id,
                    product_id = p_item_object.id,
                    product_name=p_item_object.name,
                    product_price=p_item_object.price

                        ) #we didnt use hash because now the hash gets eliminated by the bcrypt
        db.session.add(itemtocart)
        db.session.commit()
        
            

        
        
    return render_template('home.html',items=items,form=form)


@app.route('/cart')
def cart():
    
    reqprod = Cart.query.filter_by(user_id=current_user.id)
    
    
    return render_template('cart.html',reqprod=reqprod)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm() 
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(user_name=form.username.data).first() #filters out if the username entered is already in the database
        if attempted_user and attempted_user.password==form.password.data:
            login_user(attempted_user)
            flash(f'Successfully Logged In as {attempted_user.user_name}!',category='success')
            return redirect(url_for('home'))
        else:
            flash(f'Username And Password mismatch!',category='danger')

    return render_template('login.html',form=form)

@app.route('/reg',methods=['GET','POST'])
def reg():
    form=RegisterForm()  #instance of the forms
    if form.validate_on_submit(): #checks if user has clicked on submit and this happens when all validators are satisfied
        newuser = User(user_name=form.username.data,
                    phone=form.phonenumber.data,
                    email=form.emailadd.data,
                    password=form.password1.data
                        ) #we didnt use hash because now the hash gets eliminated by the bcrypt
        db.session.add(newuser)
        db.session.commit()
        flash(f'Successfully created account for {newuser.user_name}, Login using the credentials!',category='success')
        return redirect(url_for('home'))

    if form.errors != {}: #built-in dictionary field
      for err_msg in form.errors.values():
             flash(f'There was an error in creating user : {err_msg}',category='danger')
    return render_template('reg.html',form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash(f"Successfully logged out!",category="success")
    return redirect(url_for("home"))
        
@app.route('/checkout',methods=['GET','POST'])  
def checkout():
    
    form=checkoutform()  #instance of the forms
    if form.validate_on_submit: #checks if user has clicked on submit and this happens when all validators are satisfied
        neworder = ConfirmedOrders(id=random.randint(100000,999999), user_id=current_user.id) 
        db.session.add(neworder)
        db.session.commit()
        flash(f"Successfully Placed Order!",category="success")
        return redirect(url_for("home"))
        
    return render_template("checkout.html",form=form)


    