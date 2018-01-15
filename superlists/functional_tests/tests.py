''' Functional Tests 
    Author: Eric Ames
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

from django.test import LiveServerTestCase

MAX_WAIT = 10

class NewVisitorTest( LiveServerTestCase):
    browser = None

    def setUp( self):
        self.browser = webdriver.Firefox()



    def tearDown( self):
        self.browser.quit()


    def wait_and_check_for_row_in_table( self ,rowtext ,table_id):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id( table_id)
                rows = table.find_elements_by_tag_name( 'tr')
                self.assertIn( rowtext ,[row.text for row in rows])
                return
            except (AssertionError ,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep( 0.5)

    def insert_list_item( self ,entry):
        inputbox = self.browser.find_element_by_id( 'id_new_item')
        inputbox.send_keys( entry)
        inputbox.send_keys( Keys.ENTER)


    def test_start_list_and_retrieve( self):
        self.browser.get( self.live_server_url)

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

        items = [ 'Buy feathers' ,'Dye feathers']

        #User enters items and hits enter, one-by-one
        for i,item in enumerate( items):
            self.insert_list_item( item)
            self.wait_and_check_for_row_in_table( '%d: %s' % ( i+1 ,item) ,'id_list_table')



    def test_multiple_users_can_start_lists( self):
        # User E stars a new list
        self.browser.get( self.live_server_url)
        self.insert_list_item( 'Buy feathers')
        self.wait_and_check_for_row_in_table( '1: Buy feathers' ,'id_list_table')

        # User E notices her list has a unique URL
        e_list_url = self.browser.current_url
        self.assertRegex( e_list_url ,'/lists/.+')

        # User F opens up the page, without seing E's list
        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get( self.live_server_url)
        page_text = self.browser.find_element_by_tag_name( 'body').text
        self.assertNotIn( 'Buy feathers' ,page_text)
        self.assertNotIn( 'Dye feathers' ,page_text)

        # User F starts a new list, enters a new item
        self.insert_list_item( 'Buy milk')

        # Users stop
        

