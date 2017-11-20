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
    # accepts: ['MON' | 'TUE' | 'WED' | 'THU' | 'FRI' | 'SAT' | 'SUN']
    devlivery_day_of_the_week = db.Column(db.String(3))

    #beer.brewery
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'), nullable=False)

    #beer.stores and store.beers
    """
    stores is referring to the many - to - many relationship we have created with the stock table
    Example (let's say we there in information being input):
        beer1 = Beer()
        beer2 = Beer()
        beer3 = Beer()

        db.session.add(beer1)
        db.session.add(beer2)
        db.session.add(beer3)
        db.session.commit()

        store1 = Store()
        store2 = Store()

        db.session.add(store1)
        db.session.add(store2)
        db.session.commit()

        #adding to the stock table with the realtions we have
        store1.beers.append(beer1)
        store1.beers.append(beer3)
        store2.beers.append(beer2)
        store2.beers.append(beer3)

        To Query:
        for beer in store1.beers:
            print(beer.name)

    """
    #TODO: test beer.stores query like above
    stores = db.Relationship('Store', secondary=stock, backref=db.backref('beers', lazy='dynamic'))

    def __repr__(self):
        return '<Beer %r, %r, %r, %r, %r, %r, %r, %r>' % (self.name, self.brewery, self.abv, self.beer_type, self.seasonal, self.retail_cost, self.average_popularity, self.rarity)

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
        return '<Brewery %r, %r, %r, %r, %r, %r>' % (self.name, self.address, self.city, self.state, self.zip_code, self.beers)

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
        return '<Store %r, %r, %r, %r, %r, %r, %r>' % (self.name, self.address, self.city, self.state, self.zip_code, self.average_traffic, self.owner)

"""
Customer Model (these are our Users)
Customer(name, phone, email)
"""
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.Integer)
    #one email per one customer
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return '<Customer %r, %r, %r>' % (self.name, self.phone, self.email)

"""
StoreOwner Model (these are our Admins)
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
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)


    def __repr__(self):
        return '<email %r, %r, %r, %r>' % (self.name, self.phone, self.email, self.stores)

"""
Stock Table
Many Beers can be stocked at one Store. Many Stores can contain the one Beer.
"""
stock = db.Table('stock',
    db.Column('beer_id', db.Integer, db.ForeignKey('beer.id')),
    db.Column('store_id', db.Integer, db.ForeignKey('store.id'))
)
