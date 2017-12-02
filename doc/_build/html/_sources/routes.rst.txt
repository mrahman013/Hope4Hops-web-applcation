Routes
======

This page is dedicated to the routes module for our web application. This renders the templates for our web site visuals, and allows us to bring the backend to the front end in the form of jinja2 variables

Hope4Hops Pages
---------------

.. http:get:: /home

   Lists every single beer in the database in the browse table

.. http:post:: /home

   Filters the beers by style, state, availability, and rarity

.. http:get:: /about

   Renders the about page.

.. http:get:: /contact

   Renders the contacts page.

.. http:get:: /login

   Renders the login page.

.. http:post:: /login

   Checks the database for logged in user and validates with password.

.. http:get:: /logout

   Logs out the user before redirecting to the login page.

.. http:get:: /register

   Renders the register form.

.. http:post:: /register

   Creates a customer in the database after checking for validity

.. http:get:: /beerprofile?name=(String:beer_name)

   Renders the beer profile page, listing stores that sell said beer, their average traffic, and their relative distance from the user

.. http:post:: /beerprofile?name=(String:beer_name)

   Either adds a new rating for the beer or utilizes the search function to render the template

.. http:get:: /breweryprofile?name=(String:brewery_name)

   Renders the brewery profile page, listing beers that the brewery makes, and the beers various attributes

.. http:post:: /breweryprofile?name=(String:brewery_name)

   Renders the brewery profile template using the search bar function

.. http:get:: /storeprofile?name=(String:store_name)

   Renders the brewery profile page, listing beers that the store sells, along with the beer's popularity, rarity and when it normally arrives in the store

.. http:post:: /storeprofile?name=(String:store_name)

   Renders the store profile template using the search bar function

Helper Functions
----------------

.. py:function:: find_popular_beers()

   Used to find the top 3 most popular beers in the database to be placed in the home page carousel

.. py:function:: find_rare_beers()
   
   Used to find three of the rarest beers  in the database to be placed in the home page carousel

.. py:function:: staff_beers()

   Used to fill the side bar in the home page with staff reccomendations

.. py:function:: distance(lat1, lon1, lat2, lon2)

   Returns the distance in miles between two locations using their latitudes and longitudes

.. py:function:: distance_from_user(beer)

   Takes in a beer and returns a list of distances of store addresses from the user that sell beer in question

.. py:function:: login_required(f)

   Redirects the user to the login page if a page requires users to be logged in.

.. py:function:: load_user(user_id)

   Sets a customer to the current user using input user_id.

