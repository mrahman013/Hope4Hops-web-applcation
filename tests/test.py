import hopsapp
from hopsapp import app
import unittest
from flask_testing import TestCase
class hoptest(unittest.TestCase):
	def setUp(self):
		self.app = hopsapp.app.test_client()
	def test_home(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertIn('home', response.data)

if __name__=='__main__':
	unittest.main()
	

