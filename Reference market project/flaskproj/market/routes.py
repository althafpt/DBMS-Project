from market import app,db
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm,LoginForm, addtocartForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user #login required is a function that executes before the actual function, it is called a decorator

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/market', methods=['GET','POST'])
@login_required
def marketpage():
    purchase_form = addtocartForm()
    selling_form = SellItemForm
    items = Item.query.filter_by(owner=None) #only shows items that have no owner
    if request.method == "POST":
        #purchasing
        item_in_cart=request.form.get('item_in_cart') #shows all the request in the form
        p_item_object = Item.query.filter_by(name=item_in_cart).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"{p_item_object.name} has been purchased successfully, your remaining balance is {current_user.amount}",category="success")
            else:
                flash(f"Insufficient balance!", category="danger")
        
        #selling item
        sold_item = request.form.get('sold_item')
        s_item_object=Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"{s_item_object.name} has been sold successfully, your remaining balance is {current_user.amount}",category="success")
            else:
                flash(f"There was an error in selling your item!", category="danger")

        return redirect(url_for('marketpage'))
    if request.method == "GET":
        items=Item.query.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form()) #this item_name can be passed to our html using the jinja template
        

    return redirect(url_for('marketpage'))

@app.route('/register',methods=['GET','POST']) #else method not allowed to use url error comes
def registerpage():
    form=RegisterForm()  #instance of the forms
    if form.validate_on_submit(): #checks if user has clicked on submit and this happens when all validators are satisfied
        newuser = User(username=form.username.data,
                       password=form.password1.data) #we didnt use hash because now the hash gets eliminated by the bcrypt
        db.session.add(newuser)
        db.session.commit()
        login_user(newuser)
        flash(f'Successfully created account, now logged in as {newuser.username}!',category='success')
        return redirect(url_for('marketpage'))
    if form.errors != {}: #built-in dictionary field
        for err_msg in form.errors.values():
                flash(f'There was an error in creating user : {err_msg}',category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    form=LoginForm() 
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first() #filters out if the username entered is already in the database
        if attempted_user and attempted_user.check_password_correction(entered_password=form.password.data):
            login_user(attempted_user)
            flash(f'Successfully Logged In as {attempted_user.username}!',category='success')
            return redirect(url_for('marketpage'))
        else:
            flash(f'Username And Password mismatch!',category='danger')

    return render_template('login.html',form=form)



@app.route('/logout')
def logoutpage():
    logout_user()
    flash("Successfully logged out",category='info')
    return redirect(url_for("homepage")) 
