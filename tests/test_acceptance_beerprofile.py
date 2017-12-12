""" Acceptance test of searcing beer """
import unittest
import hopsapp
from bs4 import BeautifulSoup



class TestAcceptBeerProfile(unittest.TestCase):
    """
    This class test all component of beerprofile when user search for beer
    """
    def setUp(self):
        hopsapp.app.config['TESTING'] = True
        self.app = hopsapp.app.test_client()
        self.response = self.app.get("/beerprofile?name=Boat")
        self.soup = BeautifulSoup(self.response.data, 'html.parser')

    def test_beer_name(self):
        """
        Test if beer name h1 is in html page
        """
        self.assertEqual("Boat", self.soup.h1.text)

    def test_brewery_name(self):
        """
        Test if berewry name is in html page
        """
        self.assertEqual("Brewed By: CARTON BREWING COMPANY", self.soup.p.text)

    def test_beer_style(self):
        """
        Test if beer style is in html page
        """
        response = self.app.get('/beerprofile?name=Boat')
        self.assertIn(b'ALE', response.data)

    def test_beer_ABVPopuRarity(self):
        """
        Test if beer ABV, popularity, and rarity are in html page
        """
        response = self.app.get('/beerprofile?name=Boat')
        self.assertIn(b'Alcohol By Volume: 6.00%', response.data)
        self.assertIn(b'Popularity: 4.0', response.data)
        self.assertIn(b'Rarity: COMMON', response.data)

    def test_table_thread(self):
        """
        Test if table thead in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.thead.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['Store Name', 'Store Traffic', 'Delivery Day',
                   'Distance From User', 'Let\'s Go!']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)

    def test_table_tr(self):
        """
        Test if beer contents coming from database are in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.tr.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['TOP HOPS', '0', 'TUE']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)


if __name__ == '__main__':
    unittest.main()
