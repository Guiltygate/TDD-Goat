
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,redirect

from lists.models import ListItem

# Testing commit
def home_page( request):
    if request.method == 'POST':
        ListItem.objects.create( text=request.POST['item_text'] )
        return redirect('/lists/the-only-list/')
    return render( request ,'home.html')


def view_list( request):
    items = ListItem.objects.all()
    return render( request ,'list.html' ,{'items':items})