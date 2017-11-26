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
        beer_type = request.form['style']
        #refer to the state of the brewery in which the beer originates
        state = request.form['state']
        rarity = request.form['rarity']
        availability = request.form['availability']
        




    if request.method == 'POST':
        searchtype = request.form['searchtype']
        text_search = request.form['text_search']
        if searchtype == 'beer':
            return redirect(url_for('beerprofile', name=text_search))
        if searchtype == 'brewery':
            return redirect (url_for('breweryprofile', name=text_search))
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
