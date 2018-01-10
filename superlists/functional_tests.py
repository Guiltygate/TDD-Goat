''' Functional Tests 
    Author: Eric Ames
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest( unittest.TestCase):
    browser = None

    def setUp( self):
        self.browser = webdriver.Firefox()



    def tearDown( self):
        self.browser.quit()



    def test_start_list_and_retrieve( self):
        self.browser.get( 'http://localhost:8000')

        #User notices title and header are To-Do
        self.assertIn( 'To-Do' ,self.browser.title)
        header_text = self.browser.find_element_by_tag_name( 'h1').text
        self.assertIn( 'To-Do' ,header_text)


        # User is invited to enter items
        inputbox = self.browser.find_element_by_id( 'id_new_item')
        self.assertEqual(
                inputbox.get_attribute( 'placeholder')
                ,'Enter a to-do item'
        )


        # User types in item (buy feathers)
        inputbox.send_keys( 'Buy feathers')


        # User hits enter, the page updates, and the pages now lists the item
        inputbox.send_keys( Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id( 'id_list_table')
        rows = table.find_elements_by_tag_name( 'tr')
        self.assertIn( '1: Buy peacock feathers', [row.text for row in rows])


        # User still has text box for item entry. User enters item ( dye feathers)
        self.fail( 'Finish the test!')

        # Page updates again, showing both items

        # User checks if list persists, she is given a permanent URL for her list

        # User visit unique URL



if __name__ == '__main__':
    unittest.main( warnings='ignore')