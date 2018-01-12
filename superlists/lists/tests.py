from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
from lists.models import ListItem


class HomePageTest( TestCase):

    def test_home_page_returns_correct_html( self):
        response = self.client.get( '/')        
        self.assertTemplateUsed( response ,'home.html')

    def test_can_save_POST_request( self):
        response = self.client.post( '/' ,data={'item_text': 'A new list item'})

        

        self.assertIn( 'A new list item', response.content.decode())
        self.assertTemplateUsed( response ,'home.html')



class ItemModelTest( TestCase):

    def test_saving_and_retrieving_items( self):
        itemTexts = [ 'The first list item' ,'Item the second']

        for it in itemTexts:
            item = ListItem()
            item.text = it
            item.save()

        savedItems = ListItem.objects.all()
        self.assertEqual( savedItems.count() ,2)

        for count,it in enumerate(itemTexts):
            self.assertEqual( savedItems[count].text ,it)