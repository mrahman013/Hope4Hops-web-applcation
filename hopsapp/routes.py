"""Routes for flask app."""  # pylint: disable=cyclic-import
# import hashlib
from hopsapp import app
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner
from math import cos, asin, sqrt
from sqlalchemy import desc, func

def find_popular_beers():
    return Beer.query.order_by(desc(Beer.average_popularity)).limit(3)

def find_rare_beers():
    beer_r = Beer.query.order_by(func.random()).all()
    rare_beers = []
    for b in beer_r:
        if b.rarity == 'rare':
            rare_beers.append(b)
    return rare_beers[0:3]

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'GET':
        beers = Beer.query.order_by(Beer.brewery_id)
        beer_c = find_popular_beers()
        rare_beers = find_rare_beers()
        return render_template("home.html", beers=beers, beer_c=beer_c, rare_beers=rare_beers)
        # beers = Beer.query.filter(
                                    # (Beer.beer_type==beer_type)|
                                    # (Beer.brewery.has(state=state))|
                                    # (Beer.seasonal== seasonal)|
                                    # (Beer.rarity==rarity))
        # beers = Beer.query.filter(Beer.beer_type==beer_type, Beer.brewery.has(state=state), Beer.seasonal== seasonal, Beer.rarity==rarity)
        # return redirect(url_for('home', beers=beers))
    # print(request.form['submit'])
    elif request.method == 'POST':
        if request.form['submit'] == 'browse':
            beer_list = []
            beer_type = request.form['style']
            # refer to the state of the brewery in which the beer originates
            state = request.form['state']
            rarity = request.form['rarity']
            seasonal = request.form['availability']
            if seasonal=="None":
                seasonal = None
            beers = Beer.query.join(Brewery).filter_by(state=state).all()
            for b in beers:
                if (b.beer_type == beer_type) and (b.rarity == rarity) and (b.seasonal == seasonal):
                    beer_list.append(b)
            beer_c = find_popular_beers()
            rare_beers = find_rare_beers()
            return render_template("home.html", beers=beer_list, beer_c=beer_c, rare_beers=rare_beers)
            # return redirect(url_for('home', beers=beers_list, beer_c=beer_c, rare_beers=rare_beers))

        elif request.form['submit'] == 'search':
           searchtype = request.form['searchtype']
           text_search = request.form['text_search']
           if searchtype == 'beer':
               return redirect(url_for('beerprofile', name=text_search))
           if searchtype == 'brewery':
               return redirect (url_for('breweryprofile', name=text_search))
           if searchtype == 'store':
               return (url_for('storeprofile', name=text_search))

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/beerprofile', methods=['GET', 'POST'])
#value for new rating is new_rating
def beerprofile():
    if request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect(url_for('breweryprofile', name=text_search))
        if searchtype == 'store':
            return redirect(url_for('storeprofile', name=text_search))
    else:
        search = request.args['name']
        beer = Beer.query.filter_by(name=search).first()
        return render_template("beerprofile.html",beer=beer)

@app.route('/breweryprofile', methods=['GET', 'POST'])
def breweryprofile():
    if request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect(url_for('breweryprofile', name=text_search))
        if searchtype == 'store':
            return redirect(url_for('storeprofile', name=text_search))
    else:
        search = request.args['name']
        brewery = Brewery.query.filter_by(name=search).first()
        return render_template("breweryprofile.html", brewery=brewery)


@app.route('/findstore', methods=['GET', 'POST'])
def findstore():
    #TODO: get user latitude and longitude instead of using hardcoded
    user_lat = 40.8200471
    user_lon = -73.9514611
    # declaring list to hold all column of stores
    store_name = []
    store_address = []
    store_city = []
    store_state = []
    store_zip = []
    store_avg_traffic = []
    store_lat = []
    store_lon = []
    distance_from_user = []
    # geeting post's name
    search = request.args['name']
    store_search = Beer.query.filter_by(name=search)
    # loop to get data of store and put into their respective list
    for atrb in store_search:
        for element in atrb.stores:
            store_name.append(element.name)
            store_address.append(element.address)
            store_city.append(element.city)
            store_state.append(element.state)
            store_zip.append(element.zip_code)
            store_avg_traffic.append(element.average_traffic)
            store_lat.append(element.lat)
            store_lon.append(element.lon)

    #finding distance from user to store

    def distance(lat1, lon1, lat2, lon2):
        p = 0.017453292519943295     #Pi/180
        a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        return 12742 * asin(sqrt(a)) #2*R*asin...

    for i in range(len(store_lat)):
        r = distance(user_lat, user_lon, store_lat[i], store_lon[i])
        distance_from_user.append(r)

    # sorting all according to distance
    distance_from_user, store_name, store_address, store_city, store_state, store_zip, store_avg_traffic, store_lat, store_lon = zip(*sorted(zip(distance_from_user, store_name, store_address, store_city, store_state, store_zip, store_avg_traffic, store_lat, store_lon)))
    distance_from_user = [ '%.2f' % elem for elem in distance_from_user ]

    # tem2D = [{"name": "store A", "zip": 11219},
    # {"name": "store A", "zip": 11219}]
    # tem2D.append(store_name)
    # tem2D.append(store_address)

    return render_template("findstore.html", all_component = zip(store_name, store_address, store_city, store_state, store_zip, store_avg_traffic, store_lat, store_lon, distance_from_user))



@app.route('/storeprofile', methods=['GET', 'POST'])
def storeprofile():
    if request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        print(searchtype)
        print(text_search)
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect(url_for('breweryprofile', name=text_search))
        if searchtype == 'store':
            return redirect(url_for('storeprofile', name=text_search))
    else:
        search = request.args['name']
        store = Store.query.filter_by(name=search).first()
        return render_template("storeprofile.html", store=store)

"""
def average_popularity(beer, rating):

"""

# def search(method):
#     if method == 'POST':
#         searchtype = request.form['searchtype']
#         text_search = request.form['text_search']
#         if searchtype == 'beer':
#             return redirect(url_for('beerprofile', name=text_search))
#         if searchtype == 'brewery':
#             return redirect (url_for('breweryprofile'), name=text_search)

if __name__ == "__main__":
    app.run(debug=True)
