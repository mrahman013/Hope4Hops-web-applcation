"""
SQLAlchemy models
"""
#from datetime import datetime
#from flask_sqlalchemy import SQLAlchemy
from hopsapp import db

"""
Stock Table
Many Beers can be stocked at one Store. Many Stores can contain the one Beer
"""
# few things needed to disable for pylint check, such as no-member, too few public method, too many attribute
# becasue Any class we declare as inheriting from db.Model won't have query member
# until the code runs so Pylint can't detect it
#pylint: disable=no-member, too-many-instance-attributes, too-many-arguments, too-few-public-methods
stock = db.Table('stock',
                 db.Column('beer_id', db.Integer, db.ForeignKey('beer.id')),
                 db.Column('store_id', db.Integer, db.ForeignKey('store.id'))
                )


class Beer(db.Model):
    """
    Beer Model
    Beer(name, abv, beer_type, seasonal, retail_cost, average_popularity, rarity, brewery)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    #beer_image is a string that represents the link to an image associated with the row entry
    beer_image = db.Column(db.String(200), unique=True, nullable=False)
    # float represents percentage (i.e. 0.08 -> 8%)
    abv = db.Column(db.Float)
    # accepts: ['ale' | 'stout' | 'lager' | 'IPA'
    #| 'pilsner' | 'porter' | 'bitter' | 'saison', 'belgian']
    beer_type = db.Column(db.String(50))
    # accepts: ['winter' | 'spring' | 'summer' | 'autumn'| 'None']
    # value 'None' indicate all year
    seasonal = db.Column(db.String(7))
    # retail cost per unit (can or bottle)
    retail_cost = db.Column(db.Float)
    # default value will be 0
    # todo- refers to ratings to be exact but I do not want to tackle that problem at 11:54 pm
    average_popularity = db.Column(db.Float)
    # accepts: ['common' | 'uncommon' | 'rare']
    # default value for entries will be 'common'
    rarity = db.Column(db.String(10))
    # accepts: ['MON' | 'TUE' | 'WED' | 'THU' | 'FRI' | 'SAT' | 'SUN']
    devlivery_day_of_the_week = db.Column(db.String(3))
    total_ratings = db.Column(db.Integer)
    total_users = db.Column(db.Integer)
    #beer.brewery
    brewery_id = db.Column(db.Integer, db.ForeignKey('brewery.id'))

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

    # stores = db.relationship('Store', secondary=stock,
    # backref=db.backref('beers', lazy='dynamic'))
    stores = db.relationship('Store', secondary=stock, backref=db.backref('beers', lazy=True))

    def __init__(self,
                 name,
                 beer_image,
                 abv,
                 beer_type,
                 seasonal,
                 retail_cost,
                 average_popularity,
                 rarity,
                 devlivery_day_of_the_week,
                 brewery_id,
                 **kwargs):
        super(Beer, self).__init__(**kwargs)
        self.name = name
        self.beer_image = beer_image
        self.abv = abv
        self.beer_type = beer_type
        self.seasonal = seasonal
        self.retail_cost = retail_cost
        self.average_popularity = average_popularity
        self.rarity = rarity
        self.devlivery_day_of_the_week = devlivery_day_of_the_week
        self.brewery_id = brewery_id

    def __repr__(self):
        return '<Beer %r, %r, %r, %r, %r, %r, %r, %r>' % (self.name, self.brewery, self.abv, self.beer_type, self.seasonal, self.retail_cost, self.average_popularity, self.rarity) #pylint: disable=line-too-long


class Brewery(db.Model):
    """
    Brewery Model
    Brewery(name, address, city, state, zip_code)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    #accepts: state acronyms (i.e. 'NY' | 'NJ' | etc... )
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(7), nullable=False)
    # lat = db.Column(db.Float, nullable=False)
    # lon = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, unique=True)
    lon = db.Column(db.Float, unique=True)
    #brewery.beers
    # beers = db.relationship('Brewery', backref='brewery', lazy='dynamic')
    beers = db.relationship('Beer', backref='brewery', lazy=True)


    def __init__(self,
                 name,
                 address,
                 city,
                 state,
                 zip_code,
                 lat,
                 lon,
                 **kwargs):
        super(Brewery, self).__init__(**kwargs)
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.lat = lat
        self.lon = lon


    def __repr__(self):
        return '<Brewery %r, %r, %r, %r, %r, %r>' % (self.name, self.address, self.city, self.state, self.zip_code, self.beers) #pylint: disable=line-too-long


class Storeowner(db.Model):
    """
    Storeowner Model (these are our Admins)
    Storeowner(name, email, phone)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    #one email per one store owner
    email = db.Column(db.String(50), unique=True, nullable=False)
    #phone number string 20 incase international number
    phone = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=False)
    #storeowner.store
    # store = db.relationship('Store', backref='owner', lazy='dynamic')
    store = db.relationship('Store', backref='owner', lazy=True)


    def __init__(self,
                 name,
                 email,
                 phone,
                 **kwargs):
        super(Storeowner, self).__init__(**kwargs)
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '<StoreOwner %r, %r, %r, %r>' % (self.name, self.phone, self.email, self.stores)


class Store(db.Model):
    """
    Store Model
    Store(name, address, city, state, zip_code, owner)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    #accepts: state acronyms (i.e. 'NY' | 'NJ' | etc... )
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(7), nullable=False)
    # accepts: ['common' | 'uncommon' | 'rare']
    average_traffic = db.Column(db.String(10))
    # lat = db.Column(db.Float, nullable=False)
    # lon = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, unique=True)
    lon = db.Column(db.Float, unique=True)
    #store.owner
    storeowner_id = db.Column(db.Integer, db.ForeignKey('storeowner.id'))

    def __init__(self,
                 name,
                 address,
                 city,
                 state,
                 zip_code,
                 average_traffic,
                 lat,
                 lon,
                 **kwargs):
        super(Store, self).__init__(**kwargs)
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.average_traffic = average_traffic
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return '<Store %r, %r, %r, %r, %r, %r, %r>' % (self.name, self.address, self.city, self.state, self.zip_code, self.average_traffic, self.owner)#pylint: disable=line-too-long


class Customer(db.Model):
    """
    Customer Model (these are our Users)
    Customer(name, phone, email)
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    #phone number string 20 incase international number
    phone = db.Column(db.String(50), unique=True)

    #one email per one customer
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100))
    authenticated = db.Column(db.Boolean, default=True)

   # Flask-Login integration
    def is_authenticated(self):
        """
        return true for authenticated
        """
        return True

    def is_active(self): # line 37
        """
        return true for active
        """
        return True

    def is_anonymous(self):
        """
        return False
        """
        return False

    def get_id(self):
        """
        return id of user
        """
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def __init__(self, name, phone, email, password, **kwargs):
        super(Customer, self).__init__(**kwargs)
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def __repr__(self):
        return '<Customer %r, %r, %r>' % (self.name, self.phone, self.email)
