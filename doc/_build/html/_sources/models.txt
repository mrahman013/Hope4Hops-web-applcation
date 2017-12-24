Models
======

This page is dedicated to models.py, which formats our backend database. It holds the Beer, Brewery and Store Classes, as well as the Store Owner and Customer classes, each of which represents a table in our database and each of which contain methods and attributes.


Beer
----

.. py:class:: Beer(db.Model)

   .. py:method:: __init__(self,name,beer_image, abv, beer_type, seasonal, retail_cost, average_popularity, rarity, devlivery_day_of_the_week, brewery_id, **kwargs)

      Creates a beer object and sets up its attributes

   .. py:method:: __repr__(self)

      Returns the beer object as a string with all its attributes such that it can be accessed by query.

Brewery
-------

.. py:class:: Brewery(db.Model)

   .. py:method:: __init__(self, name, address, city, state, zip_code, lat, lon, **kwargs)

      Creates a brewery object and sets up its name, address and its latitude and longitude as attributes.

   .. py:method:: __repr__(self)

      Returns the brewery object as a string with all its attributes such that it can be accessed by query.

Store
-----

.. py:class:: Store(db.Model)

   .. py:method:: __init__(self, name, address, city, state, zip_code, average_traffic, lat, lon, **kwargs)

      Creates a store object and sets up its name, address and its latitude and longitude as attributes. It also has an average traffic attribute that customers can use to determine if theyre likely to get their product at that location.

   .. py:method:: __repr__(self)

      Returns the store object as a string with all its attributes such that it can be accessed by query.

Store Owner
-----------

.. py:class:: Storeowner(db.Model)

   .. py:method:: __init__(self, name, email, phone, **kwargs)

      Creates a storeowner object and sets up its name and contact information as attributes.

   .. py:method:: __repr__(self)

      Returns the store owner object as a string with all its attributes such that it can be accessed by query.


Customer
--------

.. py:class:: Customer(db.Model)
   .. py:method:: __init__(self, name, phone, email, password, **kwargs)

      Creates a customer object and sets up its name and user information as attributes.

   .. py:method:: __repr__(self)

      Returns the customer object as a string with all its attributes such that it can be accessed by query.

   .. py:method:: __unicode__(self)
      
      Returns the customer's username

   .. py:method:: is_authenticated(self)
      
      Returns true to show that a user has input his correct login information

   .. py:method:: is_active(self)

      Returns true to show activity

   .. py:method:: is_anonymous

      Returns false because anonymous is a status given to users not logged in

   .. py:method:: get_id(self)

      Returns the user's id
