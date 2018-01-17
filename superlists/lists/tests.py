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

        self.assertEqual( ListItem.objects.count() ,1)
        newItem = ListItem.objects.first()
        self.assertEqual( newItem.text ,'A new list item')

    
    def test_redirects_after_POST( self):
       response = self.client.post('/' ,data={'item_text':'A new list item'})
       self.assertEqual( response.status_code ,302)
       self.assertEqual( response['location'] ,'/lists/the-only-list/')


    def test_only_saved_items_when_needed( self):
        self.client.get('/')
        self.assertEqual( ListItem.objects.count() ,0)




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



class ListViewTest( TestCase):

    def test_uses_list_template( self):
        response = self.client.get( '/lists/the-only-list/')
        self.assertTemplateUsed( response ,'list.html')
    
    
    def test_displays_all_items( self):
        itemTexts = [ 'itemey 1' ,'itemey 2']
        for it in itemTexts:
            ListItem.objects.create( text=it)

        response = self.client.get( '/lists/the-only-list/')
        
        for it in itemTexts:
            self.assertContains( response ,it)