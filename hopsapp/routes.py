"""Routes for flask app."""  # pylint: disable= unused-import
# import hashlib
from math import cos, asin, sqrt
from functools import wraps
from operator import itemgetter, attrgetter
import json
import requests
from flask import session, request, flash, url_for, redirect, render_template, abort, g
from flask_sqlalchemy import SQLAlchemy
from hopsapp import db, app
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner
from sqlalchemy import desc, func
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required #pylint: disable=line-too-long




# flask-login

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

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
    # coordinate = coord.split(' ')
    # user_lat = float(coordinate[0])
    # user_lon = float(coordinate[1])
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
            return redirect(url_for('login'))
    return wrap

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    This method has defination of what do on landig page includes featching all beer info and
    show on home page when lending, query specifc and shown on home page when requested by user,
    redirect to appropiate routes when user search for beer, bewery or store
    """
    if request.method == 'GET':
        beers = Beer.query.order_by(Beer.brewery_id)
        beer_c = find_popular_beers()
        rare_beers = find_rare_beers()

        beer_s = staff_beers()
        return render_template("home.html", beers=beers, beer_c=beer_c, rare_beers=rare_beers, beer_s=beer_s)#pylint: disable=line-too-long

        # return render_template("home.html", beers=beers, beer_c=beer_c, rare_beers=rare_beers)

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
    return render_template("about.html")

@app.route('/contact')
def contact():
    """
    This method render contact page
    """
    return render_template("contact.html")

@login_manager.user_loader
def load_user(user_id):
    """
    This method used to query using user_id and return it
    """
    return Customer.query.get(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    This method handle login
    """
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        customer = Customer.query.filter_by(email=email, password=password).first()
        if customer is None:
            error = 'Failed Login Attempt'
            return render_template('login.html', error=error)
        login_user(customer)
        flash('Logged in successfully')
        return redirect(url_for('home'))

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    """
    This method is used to logout. It redirect to login page afrer logout
    """
    logout_user()
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

@app.route('/beerprofile', methods=['GET', 'POST'])
#value for new rating is new_rating
def beerprofile():
    """
    This method is used to show info about specfc beer's info includes distance of each store
    that carry this beer, store info, beer info. It also take care new beer rating submit by
    user
    """
    if request.method == 'GET':
        search = request.args['name']
        beer = Beer.query.filter_by(name=search).first()
        # coord = request.args['coord']

        # print('coord from beerprofile: '+ str(coord))
        # store_component = distance_from_user(beer)
        # change made hare
        # return render_template("beerprofile.html",beer=beer,all_component=store_component)
        distances = distance_from_user(beer)
        #distances = distance_from_user(beer, coord)
        return render_template("beerprofile.html", beer=beer, distances=distances)

    elif request.method == 'POST':
        if request.form['submit'] == "rating":
            search = request.args['name']
            beer = Beer.query.filter_by(name=search).first()
            # coord = request.args['coord']
            # distances = distance_from_user(beer, coord)
            distances = distance_from_user(beer)

            input_rating = request.form['new_rating']

            users = beer.total_users + 1 #int
            ratings = beer.total_ratings + int(float(input_rating)) # int
            new_average_popularity = ratings/users #float


            beer.total_users = users
            beer.total_ratings = ratings
            beer.average_popularity = new_average_popularity
            beer.rarity = rarity_system(beer)

            #fix this line so that we don't need all these lines of code
            # beer.average_popularity = new_rating(beer)

            db.session.commit()

            return render_template("beerprofile.html", beer=beer, distances=distances)

        elif request.form['submit'] == "search":
            searchtype = request.form['searchtype']
            text_search = request.form['text_search']
            # coordinates = request.form['location']
            if searchtype == 'beer':
                #return redirect(url_for('beerprofile', name=text_search, coord = coordinates))
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
    if request.method == 'GET':
        search = request.args['name']
        brewery = Brewery.query.filter_by(name=search).first()
        return render_template("breweryprofile.html", brewery=brewery)
    elif request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        #coordinates = request.form['location']
        if searchtype == 'beer':
            #return redirect(url_for('beerprofile', name=text_search, coord = coordinates))
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
    if request.method == 'GET':
        search = request.args['name']
        store = Store.query.filter_by(name=search).first()
        return render_template("storeprofile.html", store=store)
    elif request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        #coordinates = request.form['location']
        if searchtype == 'beer':
            #return redirect(url_for('beerprofile', name=text_search, coord = coordinates))
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect(url_for('breweryprofile', name=text_search))
        if searchtype == 'store':
            return redirect(url_for('storeprofile', name=text_search))

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
