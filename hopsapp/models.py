"""
SQLAlchemy models
"""
from app import db

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #name
    #brewery_id
    #type
    #seasonal
    #retail_cost
    #average_popularity
    #rarity

    def __repr__(self):
        return '<id %r>' % (self.id)

class Brewery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #name
    #address
    #city
    #state
    #zip_code

    def __repr__(self):
        return '<id %r>' % (self.id)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #name
    #address
    #city
    #state
    #zip_code
    #average_traffic

    def __repr__(self):
        return '<id %r>' % (self.id)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #name
    #email
    #phone

    def __repr__(self):
        return '<id %r>' % (self.id)

class StoreOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #store_id
    #name
    #email
    #phone

    def __repr__(self):
        return '<id %r>' % (self.id)
