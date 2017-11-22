"""Routes for flask app."""  # pylint: disable=cyclic-import
# import hashlib
from hopsapp import app
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner

@app.route('/', methods=['GET', 'POST'])
def home(beername=None, brewery=None, style=None, abv=None, popularity=None, rarity=None):
    beername="Heady Topper"
    brewery="The Alchemist"
    style="IPA"
    abv="8%"
    popularity="0"
    rarity="common"
    return render_template("home.html", beername=beername,brewery=brewery, style=style, abv=abv, popularity=popularity, rarity=rarity)

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
def beerprofile(beername=None, brewery=None, style=None, abv=None, popularity=None, rarity=None):
    beername="Heady Topper"
    brewery="The Alchemist"
    style="IPA"
    abv="8%"
    popularity="0"
    rarity="common"
    return render_template("beerprofile.html", beername=beername,brewery=brewery, style=style, abv=abv, popularity=popularity, rarity=rarity)

@app.route('/breweryprofile')
def breweryprofile(beername=None, brewery=None, style=None, abv=None, popularity=None, rarity=None):
    beername="Heady Topper"
    brewery="The Alchemist"
    style="IPA"
    abv="8%"
    popularity="0"
    rarity="common"
    return render_template("breweryprofile.html", beername=beername,brewery=brewery, style=style, abv=abv, popularity=popularity, rarity=rarity)
@app.route('/storeprofile')
def storeprofile():
    return render_template("storeprofile.html")

if __name__ == "__main__":
    app.run(debug=True)
