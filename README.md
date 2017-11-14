# Hope4Hops

Ever have that problem when a brewery released their greatest brew and can't
seem to get your hands on it? We have too! Which is why we have developed
Hope4Hops!  At the Hope4Hops team, we want to use location services to find
you and that brew you've been searching for with our easy to use interface!

### Features
-------
* use location of user to find liquor store closest to the user with the beer the user wants

![screen shot 2017-11-14 at 1 14 33 pm](https://user-images.githubusercontent.com/12536035/32797838-fb7463fc-c940-11e7-9a07-ac9890cb4164.png)

If you want to search for a specific beer, input beer name in the **Search Beer** search bar.
If you want to search by brewery, input brewery name in the **Search Brewery** search bar.
To narrow down the amount of liquor stores near you use the **Search Proximity** drop down (IN PROGRESS)

With the following input values, we will return a selection of liquor stores that contain the product you are searching for on the map.

**Happy Hunting!
Drink Responsibly!
Cheers Friends!**


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
