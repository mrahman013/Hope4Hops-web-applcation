"""Implements a basic flask app that provides hashes of text."""
from flask import Flask

app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
import hopsapp.routes

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yjjuylsytqewni:d0d63322c6abd33e2dadeafd7ef2501f73af54cf2d39596e464ea2c18b0234a3@ec2-23-23-78-213.compute-1.amazonaws.com:5432/d3gdnt7fkmonn1'

db = SQLAlchemy(app) #TODO: assure this works
# print("db: ", db) #NOTE: FOR TESTING PURPOSES, NEEDS TO BE DELETED WHEN TEST FILES CREATES
=======
app.config['DEBUG'] = True