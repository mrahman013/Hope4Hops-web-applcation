"""
SQLAlchemy models
"""
from app import db
from datetime import datetime

class Beer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), unique=True, nullable=False)
    # accepts: ['ale' | 'stout' | 'lager' | 'IPA' | 'pilsner' | 'porter' | 'bitter' | 'saison']
    beer_type=db.Column(db.String(50))
    # accepts: ['winter' | 'spring' | 'summer' | 'fall'| 'None']
    seasonal=db.Column(db.String(7))
    retail_cost=db.Column(db.Float)
    average_popularity=db.Column(db.Float)
    # accepts: ['common' | 'uncommon' | 'rare']
    rarity=db.Column(db.String(10))

    #points to a brewery_id
    brewery_id==db.Column(db.Integer, db.ForeignKey('brewery.id'),nullable=False)
    brewery=db.Relationship('Brewery', backref=db.backref('brewery',lazy=True))

    def __repr__(self):
        return '<name %r>' % (self.name)


class Brewery(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), unique=True, nullable=False)
    address=db.Column(db.String(50), unique=True, nullable=False)
    city=db.Column(db.String(50), unique=True, nullable=False)
    #accepts: state acronyms (i.e. 'NY' | 'NJ' | etc... )
    state=db.Column(db.String(2), unique=True, nullable=False)
    zip_code=db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<name %r>' % (self.name)

class Store(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), unique=True, nullable=False)
    address=db.Column(db.String(50), unique=True, nullable=False)
    city=db.Column(db.String(50), unique=True, nullable=False)
    #accepts: state acronyms (i.e. 'NY' | 'NJ' | etc... )
    state=db.Column(db.String(2), unique=True, nullable=False)
    zip_code=db.Column(db.String(50), unique=True, nullable=False)
    # accepts: ['common' | 'uncommon' | 'rare']
    average_traffic=db.Column(db.String(10))

    def __repr__(self):
        return '<name %r>' % (self.name)

class Customer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), unique=True, nullable=False)
    phone=db.Column(db.Integer)
    #one email per one customer
    email=db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<email %r>' % (self.email)

class StoreOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50), nullable=False)
    #one email per one store owner
    email=db.Column(db.String(50), unique=True, nullable=False)
    phone=db.Column(db.Integer)
    
    #points to a store_id
    store_id=db.Column(db.Integer, db.ForeignKey('store.id'),nullable=False)
    store=db.Relationship('Store', backref=db.backref('store',lazy=True))

    def __repr__(self):
        return '<email %r>' % (self.email)

#stocks table here
