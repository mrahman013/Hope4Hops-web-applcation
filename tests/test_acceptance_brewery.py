""" Acceptance test of searcing Brewery """
import unittest
import hopsapp
from bs4 import BeautifulSoup



class TestAcceptBreweryProfile(unittest.TestCase):
    """
    This class test all component of storeprofile when user search for beer
    """
    def setUp(self):
        hopsapp.app.config['TESTING'] = True
        self.app = hopsapp.app.test_client()
        self.response = self.app.get("/breweryprofile?name=The Alchemist")
        self.soup = BeautifulSoup(self.response.data, 'html.parser')

    def test_brewery_name(self):
        """
        Test if brewery name h1 is in html page
        """
        self.assertEqual("The Alchemist", self.soup.h1.text)

    def test_brewery_address(self):
        """
        Test if brewery name is in html page
        """
        response = self.app.get('/breweryprofile?name=The Alchemist')
        self.assertIn(b'Address:100 Cottage Rd', response.data)

    def test_brewery_state(self):
        """
        Test if brewery name is in html page
        """
        response = self.app.get('/breweryprofile?name=The Alchemist')
        self.assertIn(b'State:VT', response.data)


    def test_brewery_table_thread(self):
        """
        Test if table thead in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.thead.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['Beer Name', 'Style', 'ABV', 'Popularity',
                   'Rarity']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)

    def test_brewery_table_tr(self):
        """
        Test if brewery contents coming from database are in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.tr.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['Heady Topper', 'IPA', '8.00%']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)
        response = self.app.get('/breweryprofile?name=The Alchemist')
        self.assertIn(b'RARE', response.data)



        # Testing same as above with another brewery name

class TestAcceptBreweryProfile2(unittest.TestCase):
    """
    This class test all component of storeprofile when user search for beer
    """
    def setUp(self):
        hopsapp.app.config['TESTING'] = True
        self.app = hopsapp.app.test_client()
        self.response = self.app.get("/breweryprofile?name=Carton Brewing Company")
        self.soup = BeautifulSoup(self.response.data, 'html.parser')
    def test_brewery2_name(self):
        """
        Test if brewery name h1 is in html page
        """
        self.assertEqual("Carton Brewing Company", self.soup.h1.text)

    def test_brewery2_address(self):
        """
        Test if brewery name is in html page
        """
        response = self.app.get('/breweryprofile?name=Carton Brewing Company')
        self.assertIn(b'Address:6 E Washington Ave', response.data)

    def test_brewery2_state(self):
        """
        Test if brewery name is in html page
        """
        response = self.app.get('/breweryprofile?name=Carton Brewing Company')
        self.assertIn(b'State:NJ', response.data)


    def test_brewery2_table_thread(self):
        """
        Test if table thead in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.thead.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['Beer Name', 'Style', 'ABV', 'Popularity',
                   'Rarity']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)

    def test_brewery2_table_tr(self):
        """
        Test if brewery contents coming from database are in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.tr.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['077XX', 'IPA', '7.80%']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)
        response = self.app.get('/breweryprofile?name=Carton Brewing Company')
        self.assertIn(b'COMMON', response.data)



if __name__ == '__main__':
    unittest.main()
