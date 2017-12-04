import hopsapp
from hopsapp import app
import unittest
from hopsapp.routes import distance

class hoptest(unittest.TestCase):
	# def setUp(self):
	# 	self.app = hopsapp.app.test_client()
	# def test_home(self):
	# 	response = self.app.get('/')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn('home', response.data)
	# def test_about(self):
	# 	response = self.app.get('/about')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn('about', response.data)
	# def test_login(self):
	# 	response = self.app.get('/login')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn('login', response.data)
	# def test_register(self):
	# 	response = self.app.get('/register')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn('register', response.data)
	# def test_beerprofile(self):
	# 	response = self.app.get('/beerprofile')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn('beerprofile', response.data)
	# def test_breweryprofile(self):
	# 	response = self.app.get('/breweryprofile')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn('breweryprofile', response.data)
	# def test_storeprofile(self):
	# 	response = self.app.get('/storeprofile')
	# 	self.assertEqual(response.status_code, 200)
	# 	self.assertIn('storeprofile', response.data)

	# Testing distance function
	def test_distance_func(self):
		self.assertEqual(6.6, distance(40.8200471, -73.9514611, 40.727588,-73.983858))

	def test_config_debug(self):
		assert app.config['DEBUG'] is True

	# did not work
	# def test_beerprofile_intigration(self):
	# 	response = self.app.post('/', data = "Boat", follow_redirects=True)
	# 	#self.assertIn(b'Boat', response.data)
	# 	self.assertIn(b'Boat', response.data)

if __name__=='__main__':
	unittest.main()
	

