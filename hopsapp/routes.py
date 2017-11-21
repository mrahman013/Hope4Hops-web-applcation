"""Routes for flask app."""  # pylint: disable=cyclic-import
# import hashlib
from flask import render_template, request
from hopsapp import app
# print("app: ", app) #NOTE: FOR TESTING PURPOSES, NEEDS TO BE DELETED WHEN TEST FILES CREATES


# @app.route('/', methods=['GET'])
@app.route('/')
def home():
    return render_template("home.html")

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
def beerprofile():
	return render_template("beerprofile.html")

if __name__ == "__main__":
  app.run(debug=True)
