import hopsapp
from hopsapp import app
import unittest
from hopsapp import db
from hopsapp.routes import distance
from hopsapp.models import Beer, Brewery, Store, Customer, Storeowner

class hoptest(unittest.TestCase):
    def setUp(self):
        self.app = hopsapp.app.test_client()
    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('home', response.data)
    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn('about', response.data)
    def test_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('login', response.data)
    def test_register(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn('register', response.data)
    def test_beerprofile(self):
        response = self.app.get('/beerprofile')
        self.assertEqual(response.status_code, 200)
        self.assertIn('beerprofile', response.data)
    def test_breweryprofile(self):
        response = self.app.get('/breweryprofile')
        self.assertEqual(response.status_code, 200)
        self.assertIn('breweryprofile', response.data)
    def test_storeprofile(self):
        response = self.app.get('/storeprofile')
        self.assertEqual(response.status_code, 200)
        self.assertIn('storeprofile', response.data)
    def test_contact(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn('contact', response.data)
    def test_error_404(self):
        response = self.app.get('/404')
        self.assertEqual(response.status_code, 200)
        self.assertIn('404', response.data)
    def test_error_400(self):
        response = self.app.get('/400')
        self.assertEqual(response.status_code, 200)
        self.assertIn('400', response.data)
    def test_error_405(self):
        response = self.app.get('/405')
        self.assertEqual(response.status_code, 200)
        self.assertIn('405', response.data)
    def test_error_500(self):
        response = self.app.get('/500')
        self.assertEqual(response.status_code, 200)
        self.assertIn('500', response.data)




# All test below are passed

    # testing if home is getting beer name from database and showing on page when page load
    def test_home_beer_name(self):
        response = self.app.get('/')
        self.assertIn(b'HEADY TOPPER', response.data)

    # testing if home is getting Brewery name from database and showing on page when page load
    def test_home_brewery_name(self):
        response = self.app.get('/')
        self.assertIn(b'CARTON', response.data)

    # testing if home is getting beer style from database and showing on page when page load
    def test_home_beer_style(self):
        response = self.app.get('/')
        self.assertIn(b'ALE', response.data)

    # testing if home is getting beer ABV, rating, rarity from database and showing on page when page load
    def test_home_beer_others_content(self):
        response = self.app.get('/')
        self.assertIn(b'6.00%', response.data)
        self.assertIn(b'0.0', response.data)
        self.assertIn(b'COMMON', response.data)

    # Testing distance function
    def test_distance_func(self):
        self.assertEqual(6.6, distance(40.8200471, -73.9514611, 40.727588,-73.983858))

    def test_config_debug(self):
        assert app.config['DEBUG'] is True

    def test_config_database_URI(self):
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'postgres://yjjuylsytqewni:d0d63322c6abd33e2dadeafd7ef2501f73af54cf2d39596e464ea2c18b0234a3@ec2-23-23-78-213.compute-1.amazonaws.com:5432/d3gdnt7fkmonn1'

    def test_config_trackmodification(self):
        assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is True

    # did not work
    # def test_beerprofile_intigration(self):
    #     response = self.app.post('/', data = "Boat", follow_redirects=True)
    #     #self.assertIn(b'Boat', response.data)
    #     self.assertIn(b'Boat', response.data)

    #Helper functions
    def register_check(self, email, password, confirm):
        return self.app.post('/register', data=dict(email=email, password=password, confirm=confirm), follow_redirects=True)

    def login_check(self, email, password):
        return self.app.post('/login', data=dict(email=email, password=password), follow_redirects=True)

    def logout_check(self):
        return self.app.get('/logout', follow_redirects=True)

    #Testing registers
    def test_user_register(self):
        response=self.register('johndoe123@gmail.com','Password123','Password123')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cheers!', response.data)

    def test_bad_user_register(self):
        response=self.register('badexample','Password123','notthesame')
        self.assertIn(b'Ooops! We apologize! There was an error in your attempt to register.', response.data)

    #Not tested
    def test_bad_register_dupe(self):
        response=self.register('johndoe123@gmail.com','Password123','Password123')
        self.assertEqual(response.status_code,200)
        response=self.register('johndoe123@gmail.com','Pass1word123','Pass1word123')
        self.assertIn(b'Ooops! We apologize! There was an error in your attempt to register.', response.data)

    def test_login(self):
        response=self.login('johndoe@gmail.com','Password123')
        self.assertEquals(response.status_code, 200)
        self.assertIn(b'Logged in successfully',response.data)

    def test_bad_login(self):
        response=self.login('johndoe@gmail.com','passWord321')
        self.assertIn(b'Failed Login Attempt',response.data)

    def test_find_popular_beer_query(self):
        expected=['07XX','Boat','Circus Boy']
        result=self.Beer.query.order_by(desc(Beer.average_popularity)).limit(3)
        self.assertEqual(result, expected)

    #Not tested
    def test_find_rare_beer_query(self):
        expected=['SNEAKBOX','SIM-NOTIC IMPERIAL IPA','Art Hope Ale']
        result=self.Beer.query.order_by(Beer.rarity).limit(3)
        self.assertEqual(result,expected)

    def test_staff_beer_query(self):
        expected=['Heady Topper', 'SNEAKBOX', 'Feast of Fools']
        result=self.Beer.query.limit(3)
        self.assertEqual(result, expected)

if __name__=='__main__':
    unittest.main()
