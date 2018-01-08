from selenium import webdriver
import unittest

class NewVisitorTest( unittest.TestCase):
    browser = None

    def setUp( self):
        self.browser = webdriver.Firefox()

    def tearDown( self):
        self.browser.quit()

    def test_start_list_and_retrieve( self):
        self.browser.get( 'http://localhost:8000')

        #assert 'To-Do' in browser.title ,'Browser title was ' + broswer.title
        self.assertIn( 'To-Do' ,self.browser.title)

        # User is invited to enter items

        # User types in item (buy feathers)

        # User hits enter, the page updates, and the pages now lists the item

        # User still has text box for item entry. User enters item ( dye feathers)

        # Page updates again, showing both items

        # User checks if list persists, she is given a permanent URL for her list

        # User visit unique URL



if __name__ == '__main__':
    unittest.main( warnings='ignore')