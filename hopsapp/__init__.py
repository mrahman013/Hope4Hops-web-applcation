"""Implements a basic flask app that provides hashes of text."""
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yjjuylsytqewni:d0d63322c6abd33e2dadeafd7ef2501f73af54cf2d39596e464ea2c18b0234a3@ec2-23-23-78-213.compute-1.amazonaws.com:5432/d3gdnt7fkmonn1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'HGTYNVK123LOL908973'
db = SQLAlchemy(app)

# from flask_imgur import Imgur
# app.config["IMGUR_ID"] = "<katiec1029>"

import hopsapp.models
import hopsapp.routes
