import hopsapp
from hopsapp import app
import unittest

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

if __name__=='__main__':
	unittest.main()
	

