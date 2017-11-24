"""Routes for flask app."""  # pylint: disable=cyclic-import
# import hashlib
from hopsapp import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner

@app.route('/', methods=['GET', 'POST'])
def home():
    beers = Beer.query.all()
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

@app.route('/beerprofile')
def beerprofile(beer_name):
    beername="Heady Topper"
    brewery="The Alchemist"
    style="IPA"
    abv="8%"
    popularity="0"
    rarity="common"
    return render_template("beerprofile.html",
                            beername=beername,
                            brewery=brewery,
                            style=style,
                            abv=abv,
                            popularity=popularity,
                            rarity=rarity,
                            storename=storename,
                            traffic=traffic,
                            deliveryday=deliveryday)
    # beername="Heady Topper"
    # brewery="The Alchemist"
    # style="IPA"
    # abv="8%"
    # popularity="0"
    # rarity="common"
    # return render_template("beerprofile.html", beername=beername,brewery=brewery, style=style, abv=abv, popularity=popularity, rarity=rarity,storename=storename, traffic=traffic,deliveryday=deliveryday)

@app.route('/breweryprofile')
def breweryprofile(brewery_name):

    return render_template("breweryprofile.html", )

    # beername="Heady Topper"
    # brewery="The Alchemist"
    # style="IPA"
    # abv="8%"
    # popularity="0"
    # rarity="common"
    # return render_template("breweryprofile.html", beername=beername,brewery=brewery, style=style, abv=abv, popularity=popularity, rarity=rarity, address=address,state=state)


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


if __name__ == "__main__":
    app.run(debug=True)
