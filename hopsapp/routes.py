"""Routes for flask app."""  # pylint: disable=cyclic-import
# import hashlib
from flask import render_template, request
from hopsapp import app
print("app: ", app) #NOTE: FOR TESTING PURPOSES, NEEDS TO BE DELETED WHEN TEST FILES CREATES


# @app.route('/', methods=['GET'])
@app.route('/')
def home():
    return render_template("home.html")

# @app.route('/about')
# def about():
#     return render_template("")  #insert name of template here

if __name__ == "__main__":
  app.run(debug=True)
