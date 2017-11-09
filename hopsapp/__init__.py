"""Implements a basic flask app that provides hashes of text."""
from flask import Flask
app = Flask(__name__)
import hopsapp.routes
