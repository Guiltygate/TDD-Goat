
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,redirect

from lists.models import ListItem

def home_page( request):
    if request.method == 'POST':
        ListItem.objects.create( text=request.POST['item_text'] )
        return redirect('/')

    items = ListItem.objects.all()
    return render( request ,'home.html' ,{'items':items})