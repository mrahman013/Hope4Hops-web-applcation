"""Implements a basic flask app that provides hashes of text."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import flask_login
#pylint: disable=invalid-name
app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yjjuylsytqewni:d0d63322c6abd33e2dadeafd7ef2501f73af54cf2d39596e464ea2c18b0234a3@ec2-23-23-78-213.compute-1.amazonaws.com:5432/d3gdnt7fkmonn1' #pylint: disable=line-too-long
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'HGTYNVK123LOL908973'
db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# This import need to be here that's why disabling pylint
#pylint: disable=wrong-import-position
import hopsapp.models
import hopsapp.routes
