"""Routes for flask app."""  # pylint: disable=cyclic-import
import hashlib
from flask import render_template
from flask import request
from mathapp import app


@app.route('/', methods=['GET'])
def index():
    return render_template("")  #insert name of template here

@app.route('/about')
def about():
    return render_template("")  #insert name of template here
