# Hope4Hops

Ever have that problem when a brewery released their greatest brew and can't
seem to get your hands on it? We have too! Which is why we have developed
Hope4Hops!  At the Hope4Hops team, we want to use location services to find
you and that brew you've been searching for with our easy to use interface!

### Overview
-------


If you want to search for a specific beer, input beer name in the **Search Beer** search bar.

If you want to search by brewery, input brewery name in the **Search Brewery** search bar.

With the following input values, we will return a selection of liquor stores that contain the product you are searching for on the map.

**Happy Hunting!**

**Drink Responsibly!**

**Cheers Friends!**


### Installation
-------
* create a virtual env (virtualenv .venv)
* source .venv/bin/activate
* pip3 install -r requirements.txt
* pip install -e .

### Running the dev server locally
-------
* Navigate to root directory of this project
* Run these commands once
  * export FLASK_DEBUG=true
  * export FLASK_APP=hopsapp

* Run this line every time you want to start the server
  * flask run

* Other way is to run `python app.py` on root directory

### Running tests
-------
* Unit and Integration tests
  * Navigate to /tests
    * python test.py -v
* Acceptance test of searcing Beer and Beer Profile
  * Navigate to /tests
    * python test_acceptance_beerprofile.py -v
    
 * Acceptance test of searcing Brewery and Brewery Profile
  * Navigate to /tests
    * python test_acceptance_brewery.py -v
    
* Acceptance test of searcing Store and Store Profile
  * Navigate to /tests
    * python test_acceptance_storeprofile.py -v
    
 
### Contribute
-------
Issue Tracker: https://github.com/katierose1029/Hope4Hops/issues

Source Code: https://github.com/katierose1029/Hope4Hops

### Support
-------
If you are having issues, please let us know.

### License
-------
The project is licensed under the MIT license.
