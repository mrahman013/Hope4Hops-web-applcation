"""Routes for flask app."""  # pylint: disable=cyclic-import
# import hashlib
from hopsapp import app
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner
# from flask_imgur import Imgur

@app.route('/', methods=['GET', 'POST'])
def home():
    beers = Beer.query.all()
    if request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect (url_for('breweryprofile', name=text_search))

        if searchtype == 'store':
            return redirect (url_for('findstore', name=text_search))
    return render_template("home.html", beers=beers)

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
def beerprofile():
    search = request.args['name']
    beer = Beer.query.filter_by(name=search).first()
    if request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect (url_for('breweryprofile', name=text_search))

    return render_template("beerprofile.html",beer=beer)

@app.route('/breweryprofile', methods=['GET', 'POST'])
def breweryprofile():
    search = request.args['name']
    brewery = Brewery.query.filter_by(name=search).first()
    if request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect(url_for('breweryprofile'), name=text_search)
    return render_template("breweryprofile.html", brewery=brewery)


@app.route('/findstore', methods=['GET', 'POST'])
def findstore():
    # declaring list to hold all column of stores
    store_name = []
    store_address = []
    store_city = []
    store_state = []
    store_zip = []
    store_avg_traffic = []
    store_lat = []
    store_lon = []
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
    print(store_name)
    print(store_address)
    print(store_city)
    print(store_state)
    print(store_zip)
    print(store_avg_traffic)
    print(store_lat)
    print(store_lon)
    return render_template("findstore.html")

@app.route('/storeprofile')
def storeprofile(beername=None, brewery=None, style=None, abv=None, popularity=None, rarity=None,address=None, state=None, storename=None, traffic=None,deliverday=None):
    beername="Heady Topper"
    brewery="The Alchemist"
    style="IPA"
    abv="8%"
    popularity="0"
    rarity="common"
    return render_template("storeprofile.html", beername=beername,brewery=brewery, style=style, abv=abv, popularity=popularity, rarity=rarity, address=address,state=state, storename=storename, traffic=traffic,deliveryday=deliveryday)

"""
def average_popularity(beer, rating):

"""

def search(method):
    if method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect (url_for('breweryprofile'), name=text_search)

if __name__ == "__main__":
    app.run(debug=True)
