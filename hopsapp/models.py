"""
SQLAlchemy models
"""
from datetime import datetime
from hopsapp import db



"""
Beer Model
Beer(name, abv, beer_type, seasonal, retail_cost, average_popularity, rarity, brewery)
"""
class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    # accepts: ['ale' | 'stout' | 'lager' | 'IPA' | 'pilsner' | 'porter' | 'bitter' | 'saison']
    abv = db.Column(db.Float)
    beer_type = db.Column(db.String(50))
    # accepts: ['winter' | 'spring' | 'summer' | 'fall'| 'None']
    seasonal = db.Column(db.String(7))
    retail_cost = db.Column(db.Float)
    average_popularity = db.Column(db.Float)
    # accepts: ['common' | 'uncommon' | 'rare']
    rarity = db.Column(db.String(10))
    #beer.brewery
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'), nullable=False)

    def __repr__(self):
        return '<name %r>' % (self.name)

"""
Brewery Model
Brewery(name, address, city, state, zip_code)
"""
class Brewery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), unique=True, nullable=False)
    #accepts: state acronyms (i.e. 'NY' | 'NJ' | etc... )
    state = db.Column(db.String(2), unique=True, nullable=False)
    zip_code = db.Column(db.String(50), unique=True, nullable=False)
    #brewery.beers
    beers = db.Relationship('Brewery', backref='brewery', lazy='dynamic')

    def __repr__(self):
        return '<name %r>' % (self.name)

"""
Store Model
Store(name, address, city, state, zip_code, owner)
"""
class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    #accepts: state acronyms (i.e. 'NY' | 'NJ' | etc... )
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(50), nullable=False)
    # accepts: ['common' | 'uncommon' | 'rare']
    average_traffic = db.Column(db.String(10))
    #store.owner
    store_owner_id = db.Column(db.Integer, db.ForeignKey('storeowner.id'))

    def __repr__(self):
        return '<name %r>' % (self.name)

"""
Customer Model
Customer(name, phone, email)
"""
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.Integer)
    #one email per one customer
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return '<email %r>' % (self.email)

"""
StoreOwner Model
StoreOwner(name, email, phone)
"""
class StoreOwner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    #one email per one store owner
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.Integer)
    #storeowner.store
    store = db.Relationship('Store', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<email %r>' % (self.email)

"""
"""
#stocks table here
