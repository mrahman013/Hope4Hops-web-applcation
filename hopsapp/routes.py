"""Routes for flask app."""  # pylint: disable= unused-import
# import hashlib
from math import cos, asin, sqrt
from functools import wraps
from operator import itemgetter, attrgetter
import json
import requests
from flask import session, request, Response, flash, url_for, redirect, render_template, abort, g
from flask_sqlalchemy import SQLAlchemy
from hopsapp import db, app
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner
from sqlalchemy import desc, func
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required #pylint: disable=line-too-long
from flask_principal import Principal, Permission, RoleNeed

# Any class we declare as inheriting from db.Model won't have query member
# until the code runs so Pylint can't detect it
#pylint: disable=no-member
# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#flask-principal
principals = Principal(app)
#flask-permissions
perms = Permission(app, db, current_user)

#A terrible hack job to determine whether a storeowner or customer
#are logged in, in the future, this is never to be done
LOGGED_IN = None


# Create a permission with a single Need, in this case a RoleNeed.
# storeowner_permission = Permission(RoleNeed('storeowner'))
# print('storeowner_permission ', storeowner_permission)

def find_popular_beers():
    """
    This method is used to query beer's average popularity
    """
    return Beer.query.order_by(desc(Beer.average_popularity)).limit(3)

def find_rare_beers():
    """
    This method is used to query rare beer. It return list with 3 rare beer that is found
    from database
    """
    beer_r = Beer.query.order_by(func.random()).all()
    rare_beers = []
    for beer in beer_r:
        if beer.rarity == 'rare':
            rare_beers.append(beer)
    return rare_beers[0:3]

#todo- finish this to reduce code
# def new_rating(beer):
#     users = beer.total_users + 1 #int
#     ratings = beer.total_ratings + int(float(input_rating)) # int
#     new_average_popularity = ratings/users #float

#create a percentage of users that rate this beer
#if more than 50% of users have had the beer, it is considered common
#between 25% and 50% is considered uncommon
# less than 25% is consdiered rare
def rarity_system(beer):
    """
    This method determine rarity of beer
    """
    users = len(Customer.query.all())
    beer_users = beer.total_users
    total_users = users + beer_users
    #precent
    per = beer_users/total_users
    if 0.5 < per <= 1:
        return "common"
    elif 0.25 <= per <= 0.5:
        return "uncommon"
    elif per < 0.25:
        return "rare"

def staff_beers():
    """
    This method is used to return 3 beer
    """
    return Beer.query.limit(3)

def distance(lat1, lon1, lat2, lon2):
    """
    This method is used to find distance between 2 coordinates and retund distance in miles
    """
    conv_fac = 0.621371 # conversion factor
    pi_red = 0.017453292519943295     #Pi/180
    reulst_dis = 0.5 - cos((lat2 - lat1) * pi_red)/2 + cos(lat1 * pi_red) * cos(lat2 * pi_red) * (1 - cos((lon2 - lon1) * pi_red)) / 2 #pylint: disable=line-too-long
    kil_m = 12742 * asin(sqrt(reulst_dis))
    miles = kil_m * conv_fac
    miles = float("{0:.1f}".format(miles))
    return miles

def distance_from_user(beer):
    """
    This method is used to calculate distace from user to each store that carry
    specific beer that user seached for and return list of store, beer and distance from user to
    those stores sorted by distance
    """
    # user_lat = 40.8200471
    # user_lon = -73.9514611
    send_url = 'http://freegeoip.net/json'
    req = requests.get(send_url)
    j = json.loads(req.text)
    user_lat = j['latitude']
    user_lon = j['longitude']

    distances = []

    for store in beer.stores:
        dist = distance(user_lat, user_lon, store.lat, store.lon)
        distances.append((beer, store, dist))

    sorted_distances = sorted(distances, key=itemgetter(2))
    return sorted_distances

def login_required(f):
    """
    This method is used to call wrap function which has instruction what to do when user
    loged in or not
    """
    @wraps(f)
    def wrap(*args, **kwargs):
        """
        This method is used to make sure user is loggen in and if not alert to login and
        redirect to login page
        """
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('home'))
    return wrap

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    This method has defination of what do on landig page includes featching all beer info and
    show on home page when lending, query specifc and shown on home page when requested by user,
    redirect to appropiate routes when user search for beer, bewery or store
    """
    print(LOGGED_IN)
    if request.method == 'GET':
        beers = Beer.query.order_by(Beer.brewery_id)
        beer_c = find_popular_beers()
        rare_beers = find_rare_beers()
        beer_s = staff_beers()
        return render_template("home.html", beers=beers, beer_c=beer_c, rare_beers=rare_beers, beer_s=beer_s)#pylint: disable=line-too-long

    elif request.method == 'POST':
        if request.form['submit'] == 'browse':
            beer_list = []
            beer_type = request.form['style']
            # refer to the state of the brewery in which the beer originates
            state = request.form['state']
            rarity = request.form['rarity']
            seasonal = request.form['availability']
            if seasonal == "None":
                seasonal = None
            beers = Beer.query.join(Brewery).filter_by(state=state).all()
            for b in beers:
                if (b.beer_type == beer_type) and (b.rarity == rarity) and (b.seasonal == seasonal):
                    beer_list.append(b)
            beer_c = find_popular_beers()
            rare_beers = find_rare_beers()
            beer_s = staff_beers()
            return render_template("home.html", beers=beer_list, beer_c=beer_c, rare_beers=rare_beers, beer_s=beer_s)#pylint: disable=line-too-long
        elif request.form['submit'] == 'search':
            searchtype = request.form['searchtype']
            text_search = request.form['text_search']
            # coordinates added
            # coordinates = request.form['location']
            print(text_search)
            if searchtype == 'beer':
               #return redirect(url_for('beerprofile', name=text_search, coord = coordinates))
                return redirect(url_for('beerprofile', name=text_search))
            if searchtype == 'brewery':
                return redirect(url_for('breweryprofile', name=text_search))
            if searchtype == 'store':
                return redirect(url_for('storeprofile', name=text_search))

@app.route('/about')
def about():
    """
    This method render about page and disply it
    """
    print(LOGGED_IN)
    return render_template("about.html")

@app.route('/contact')
def contact():
    """
    This method render contact page
    """
    print(LOGGED_IN)
    return render_template("contact.html")

@login_manager.user_loader
def load_user(user_id):
    """
    This method used to query using user_id and return it
    """
    try:
        if LOGGED_IN == 'customer':
            return Customer.query.get(user_id)
        elif LOGGED_IN == 'storeowner':
            return Storeowner.query.get(user_id)
    except:
        return None
    # customers = Customer.query.all()
    # storeowners = Storeowner.query.all()
    # return Customer.query.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    This method handle login
    """
    global LOGGED_IN
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        usertype = request.form['usertype']
        if usertype == "customer":
            email = request.form['email']
            password = request.form['password']
            customer = Customer.query.filter_by(email=email, password=password).first()
            if customer is None:
                error = 'Failed Login Attempt'
                return render_template('login.html', error=error)
            login_user(customer)
            # print(type(current_user))
            # print(isinstance(current_user, Customer))
            # global LOGGED_IN = 'customer'
            LOGGED_IN = 'customer'
            # set_LOGGED_IN('customer')
            print(LOGGED_IN)
            flash('Welcome ' + customer.name)
            return redirect(url_for('home'))
        elif usertype == "storeowner":
            email = request.form['email']
            password = request.form['password']
            storeowner = Storeowner.query.filter_by(email=email, password=password).first()
            if storeowner is None:
                error = 'Failed Login Attempt'
                return render_template('login.html', error=error)
            login_user(storeowner)
            # global LOGGED_IN = 'storeowner'
            LOGGED_IN = 'storeowner'
            # set_LOGGED_IN('storeowner')
            print(LOGGED_IN)
            flash('Welcome ' + storeowner.name)
            return redirect(url_for('home'))

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    """
    This method is used to logout. It redirect to login page afrer logout
    """
    global LOGGED_IN
    LOGGED_IN = None
    logout_user()
    flash('Successfully Logged Out')
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    This method is used to handle registration of new user. It takes all necessary info of
    user and try to put on customer table if don't exist
    """
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        if request.form['submit'] == "register":
            if request.form['confirm_password'] != request.form['password']:
                flash('Passwords DO NOT Match')
                return render_template("register.html")
            usertype = request.form['usertype']
            if usertype == "customer":
                name = request.form['name']
                phone = request.form['phone']
                email = request.form['email']
                password = request.form['password']
                new_customer = Customer(name=name, phone=phone, email=email, password=password)
                try:
                    db.session.add(new_customer)
                    db.session.commit()
                    flash('Cheers! ' + name)
                    return redirect(url_for('home'))
                #pylint: disable=bare-except
                except:
                    error = 'Ooops! We apologize! There was an error in your attempt to register.'#pylint: disable=unused-variable
                    return redirect(url_for('home'))
            elif usertype == "storeowner":
                name = request.form['name']
                phone = request.form['phone']
                email = request.form['email']
                password = request.form['password']
                print(password)
                new_storeowner = Storeowner(name=name, phone=phone, email=email, password=password)
                try:
                    db.session.add(new_storeowner)
                    db.session.commit()
                    flash('Cheers! ' + name)
                    return redirect(url_for('home'))
                #pylint: disable=bare-except
                except:
                    error = 'Ooops! We apologize! There was an error in your attempt to register.'#pylint: disable=unused-variable
                    return redirect(url_for('home'))

@app.route('/beerprofile', methods=['GET', 'POST'])
#value for new rating is new_rating
def beerprofile():
    """
    This method is used to show info about specfc beer's info includes distance of each store
    that carry this beer, store info, beer info. It also take care new beer rating submit by
    user
    """
    print(LOGGED_IN)
    if request.method == 'GET':
        search = request.args['name']
        beer = Beer.query.filter_by(name=search).first()

        distances = distance_from_user(beer)
        return render_template("beerprofile.html", beer=beer, distances=distances)

    elif request.method == 'POST':
        if request.form['submit'] == "rating":
            search = request.args['name']
            beer = Beer.query.filter_by(name=search).first()
            distances = distance_from_user(beer)

            input_rating = request.form['new_rating']

            users = beer.total_users + 1 #int
            ratings = beer.total_ratings + int(float(input_rating)) # int
            new_average_popularity = ratings/users #float

            beer.total_users = users
            beer.total_ratings = ratings
            beer.average_popularity = new_average_popularity
            beer.rarity = rarity_system(beer)

            db.session.commit()

            return render_template("beerprofile.html", beer=beer, distances=distances)

        elif request.form['submit'] == "search":
            searchtype = request.form['searchtype']
            text_search = request.form['text_search']
            if searchtype == 'beer':
                return redirect(url_for('beerprofile', name=text_search))
            if searchtype == 'brewery':
                return redirect(url_for('breweryprofile', name=text_search))
            if searchtype == 'store':
                return redirect(url_for('storeprofile', name=text_search))

@app.route('/breweryprofile', methods=['GET', 'POST'])
def breweryprofile():
    """
    This method is used to show info about specfc bewery info includes all beers they produce and
    their style, ABV, popularity and rarity
    """
    print(LOGGED_IN)
    if request.method == 'GET':
        search = request.args['name']
        brewery = Brewery.query.filter_by(name=search).first()
        return render_template("breweryprofile.html", brewery=brewery)
    elif request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect(url_for('breweryprofile', name=text_search))
        if searchtype == 'store':
            return redirect(url_for('storeprofile', name=text_search))

@app.route('/storeprofile', methods=['GET', 'POST'])
def storeprofile():
    """
    This method is used to show info about specfc store's info includes all beers they carry and
    their style, ABV, popularity and rarity
    """
    print(LOGGED_IN)
    if request.method == 'GET':
        search = request.args['name']
        store = Store.query.filter_by(name=search).first()
        return render_template("storeprofile.html", store=store)
    elif request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect(url_for('breweryprofile', name=text_search))
        if searchtype == 'store':
            return redirect(url_for('storeprofile', name=text_search))

@app.route('/addbeer', methods=['GET', 'POST'])
def add_beer():
    """
    store owner privilege access only
    add a beer to a store by a store owner
    """
    print(LOGGED_IN)
    if LOGGED_IN is not 'storeowner':
        flash('Must be a storeowner')
        return redirect(url_for('home'))

    if request.method == 'POST':
        beer_name = request.form['beer_name']

        #check if we have beer on file
        if Beer.query.filter_by(name=beer_name):
            beer = Beer.query.filter_by(name=beer_name).first()
            beer_store = request.form['beer_store']
            store = Store.query.filter_by(name=beer_store).first()
            store.beers.append(beer)
            db.session.commit()
            flash('Beer added successfully to your store ' + current_user.name)
            return redirect(url_for('home'))

        beer_brewery = request.form['beer_brewery']
        beer_abv = request.form['beer_abv']
        beer_type = request.form['beer_type']
        beer_seasonal = request.form['beer_seasonal']
        #query the store and then append
        beer_store = request.form['beer_store']
        beer_retail_cost = request.form['beer_retail_cost']
        beer_image = request.form['beer_image']
        beer_delivery_day_of_the_week = request.form['beer_delivery_day_of_the_week']

        brewery = Brewery.query.filter_by(name=beer_brewery).first()
        store = Store.query.filter_by(name=beer_store).first()
        new_beer = Beer(name=beer_name,
                        beer_image=beer_image,
                        abv=beer_abv,
                        beer_type=beer_type,
                        seasonal=beer_seasonal,
                        retail_cost=beer_retail_cost,
                        devlivery_day_of_the_week=beer_delivery_day_of_the_week,
                        brewery_id=brewery.id)

        #add the new beer to the db
        db.session.add(new_beer)
        #commit the data to the database
        db.session.commit()
        #add the beer to the list of beers of the store
        store.beers.append(new_beer)
        db.session.commit()

        flash('Beer added successfully to your store ' + current_user.name)
        return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template("addbeer.html")

@app.route('/addstore', methods=['GET', 'POST'])
def add_store():
    """
    store owner privilege access only
    add a beer to a store by a store owner
    """
    #uncomment when testing logged in storeowner
    if LOGGED_IN == 'customer' or LOGGED_IN == None:
        flash('Must be a storeowner')
        return redirect(url_for('home'))

    if request.method == 'POST':
        name = request.form['store_name']
        address = request.form['store_address']
        city = request.form['store_city']
        state = request.form['store_state']
        zip_code = request.form['store_zip_code']
        #for this we must assume that a storeowner is logged in
        # and that storeowner has an id
        storeowner_id = current_user.id

        store = Store(name=name,
                      address=address,
                      city=city,
                      state=state,
                      zip_code=zip_code,
                      storeowner_id=storeowner_id)

        db.session.add(store)
        db.session.commit()
        flash('Added your store successfully')
        return redirect(url_for('home'))

    elif request.method == 'GET':
        return render_template("addstore.html")

#Error handler
@app.errorhandler(404)
def not_found_error(error):
    """
    handle not found error code status 404
    """
    return render_template('404.html'), 404

@app.errorhandler(405)
def not_found_error(error):
    """
    handle not found error code status 405
    """
    return render_template('405.html'), 405

@app.errorhandler(400)
def not_found_error(error):
    """
    handle not found error code status 400
    """
    return render_template('400.html'), 400

@app.errorhandler(500)
def internal_error(error):
    """
    handle internal error code status 500
    """
    db.session.rollback()
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)
