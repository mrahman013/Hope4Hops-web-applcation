import hopsapp
from hopsapp import app
import unittest
from bs4 import BeautifulSoup
import os.path as op
import os
from hopsapp.routes import distance


class TestAcceptBeerProfile(unittest.TestCase):
	def setUp(self):
		hopsapp.app.config['TESTING'] = True
		self.app = hopsapp.app.test_client()
		self.response = self.app.get("/beerprofile?name=Boat")
		self.soup = BeautifulSoup(self.response.data,'html.parser')

	def test_beerprofile_beer_name(self):
		self.assertEqual("Boat",self.soup.h1.text)

	def test_beerprofile_brewery_name(self):
		self.assertEqual("Brewed By: CARTON BREWING COMPANY",self.soup.p.text)

	def test_beerprofile_beer_style(self):
		response = self.app.get('/beerprofile?name=Boat')
		self.assertIn(b'ALE', response.data)

	def test_beerprofile_beer_ABV_popu_rarity(self):
		response = self.app.get('/beerprofile?name=Boat')
		self.assertIn(b'Alcohol By Volume: 6.00%', response.data)
		self.assertIn(b'Popularity: 4.0', response.data)
		self.assertIn(b'Rarity: COMMON', response.data)

	def test_beerprofile_all_info_on_table_thread(self):
		table = self.soup.table
		self.assertTrue(table)
		items_td = table.thead.find_all('td')
		self.assertEqual(5, len(items_td))
		# list of td for check
		list_td = ['Store Name', 'Store Traffic', 'Delivery Day', 'Distance From User', 'Let\'s Go!']
		for item, ele_list in zip(items_td, list_td):
			self.assertEqual(item.text.strip(), ele_list)

	def test_beerprofile_all_info_on_table_tr(self):
		table = self.soup.table
		self.assertTrue(table)
		items_td = table.tr.find_all('td')
		self.assertEqual(5, len(items_td))
		# list of td for check
		list_td = ['TOP HOPS', '0', 'TUE']
		for item, ele_list in zip(items_td, list_td):
			self.assertEqual(item.text.strip(), ele_list)


if __name__=='__main__':
	unittest.main()