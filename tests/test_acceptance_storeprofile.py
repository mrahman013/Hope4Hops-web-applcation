""" Acceptance test of searcing store """
import unittest
import hopsapp
from bs4 import BeautifulSoup



class TestAcceptStoreProfile(unittest.TestCase):
    """
    This class test all component of storeprofile when user search for beer
    """
    def setUp(self):
        hopsapp.app.config['TESTING'] = True
        self.app = hopsapp.app.test_client()
        self.response = self.app.get("/storeprofile?name=Top Hops")
        self.soup = BeautifulSoup(self.response.data, 'html.parser')

    def test_store_name(self):
        """
        Test if store name h1 is in html page
        """
        self.assertEqual("Top Hops", self.soup.h1.text)

    def test_store_address(self):
        """
        Test if store name is in html page
        """
        response = self.app.get('/storeprofile?name=Top Hops')
        self.assertIn(b'Address: 94 Orchard St', response.data)

    def test_store_state(self):
        """
        Test if store name is in html page
        """
        response = self.app.get('/storeprofile?name=Top Hops')
        self.assertIn(b'State: NY', response.data)

    def test_store_traffic(self):
        """
        Test if store name is in html page
        """
        response = self.app.get('/storeprofile?name=Top Hops')
        self.assertIn(b'Traffic: ', response.data)



    def test_store_table_thread(self):
        """
        Test if table thead in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.thead.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['Beer Name', 'Brewery', 'Popularity',
                   'Rarity', 'Delivery Day']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)

    def test_store_table_tr(self):
        """
        Test if store contents coming from database are in html page
        """
        table = self.soup.table
        self.assertTrue(table)
        items_td = table.tr.find_all('td')
        self.assertEqual(5, len(items_td))
        # list of td for check
        list_td = ['Focal Banger', 'The Alchemist']
        for item, ele_list in zip(items_td, list_td):
            self.assertEqual(item.text.strip(), ele_list)

    def test_store_random_contents(self):
        """
        Test if store name is in html page
        """
        response = self.app.get('/storeprofile?name=Top Hops')
        self.assertIn(b'Circus Boy', response.data)
        self.assertIn(b'Magic Hat Brewing Company', response.data)
        self.assertIn(b'MON', response.data)
        self.assertIn(b'Art Hop Ale', response.data)
        self.assertIn(b'AMERICAN PALE ALE', response.data)
        self.assertIn(b'Cricket Hill Brewery', response.data)
        self.assertIn(b'COMMON', response.data)
        self.assertIn(b'THU', response.data)
        self.assertIn(b'RARE', response.data)


if __name__ == '__main__':
    unittest.main()
