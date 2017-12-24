""" Unit and intergation tests """
import unittest
import hopsapp
from hopsapp import app
from bs4 import BeautifulSoup
from hopsapp.routes import distance


class TestUnitHopsapp(unittest.TestCase):
    """ Unit test class """
    def setUp(self):
        """
        setup for unit test
        """
        hopsapp.app.config['TESTING'] = True
        self.app = hopsapp.app.test_client()
        self.response = self.app.get("/")
    def test_home(self):
        """ test home status code """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        #self.assertIn('home', response.data)
    def test_about(self):
        """ test about page status code """
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        #self.assertIn('about', response.data)
    def test_login(self):
        """ test login page status code """
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        #self.assertIn('login', response.data)
    def test_register(self):
        """ test register page status code """
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        #self.assertIn('register', response.data)
    def test_beerprofile(self):
        """ test beerprofile page status code """
        response = self.app.get('/beerprofile?name=Boat')
        self.assertEqual(response.status_code, 200)
        #         self.assertIn('beerprofile', response.data)
    def test_breweryprofile(self):
        """ test breweryprofile status code """
        response = self.app.get('/breweryprofile?name=Carton Brewing Company')
        self.assertEqual(response.status_code, 200)
        #         self.assertIn('breweryprofile', response.data)
    def test_storeprofile(self):
        """ test storeprofile page status code """
        response = self.app.get('/storeprofile?name=Good Beer')
        self.assertEqual(response.status_code, 200)
        #         self.assertIn('storeprofile', response.data)
    def test_contact(self):
        """ test contact page status code """
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_distance_func(self):
        """ testing distance function """
        self.assertEqual(6.6, distance(40.8200471, -73.9514611, 40.727588, -73.983858))

    def test_config_debug(self):
        """ testing debug config is true """
        assert app.config['DEBUG'] is True

    def test_configdb_uri(self):
        """ testing DB uri """
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgres://yjjuylsytqewni:d0d63322c6abd33e2dadeafd7ef2501f73af54cf2d39596e464ea2c18b0234a3@ec2-23-23-78-213.compute-1.amazonaws.com:5432/d3gdnt7fkmonn1'

    def test_config_trackmodification(self):
        """ testing trackmodification config is true """
        assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is True

    def test_error_400(self):
        """ test error status """
        response = self.app.get('/400')
        self.assertEqual(response.status_code, 404)
        # self.assertIn('400', response.data)

    def test_error_405(self):
        """ test error status """
        response = self.app.get('/405')
        self.assertEqual(response.status_code, 404)
        # self.assertIn('405', response.data)

    def test_error_500(self):
        """ test error status """
        response = self.app.get('/500')
        self.assertEqual(response.status_code, 404)
        # self.assertIn('500', response.data)





class TestIntegration(unittest.TestCase):
    """ Integration test class """
    def setUp(self):
        """ setup for integration test """
        hopsapp.app.config['TESTING'] = True
        self.app = hopsapp.app.test_client()
        self.response = self.app.get("/")
        self.soup = BeautifulSoup(self.response.data, 'html.parser')

    def test_home_beer_name(self):
        """ testing if home is getting beer name from database and
        showing on page when page load
        """
        response = self.app.get('/')
        self.assertIn(b'HEADY TOPPER', response.data)

    def test_home_brewery_name(self):
        """
        testing if home is getting Brewery name from database
        and showing on page when page load
        """
        response = self.app.get('/')
        self.assertIn(b'CARTON', response.data)

    def test_home_beer_style(self):
        """
        testing if home is getting beer style from database
        and showing on page when page load
        """
        response = self.app.get('/')
        self.assertIn(b'ALE', response.data)

    def test_homebeer_abv(self):
        """
        testing if home is getting beer ABV from database
        and showing on page when page load
        """
        response = self.app.get('/')
        self.assertIn(b'6.00%', response.data)


    def test_home_beer_rating(self):
        """
        testing if home is getting beer rating from database
        and showing on page when page load
        """
        response = self.app.get('/')
        self.assertIn(b'0.0', response.data)

    def test_home_beer_rarity(self):
        """
        testing if home is getting beer rarity from database
        and showing on page when page load
        """
        response = self.app.get('/')
        self.assertIn(b'COMMON', response.data)



if __name__ == '__main__':

    unittest.main()
