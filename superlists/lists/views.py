
from django.shortcuts import render
from django.http import HttpResponse



hpHTML = '''<html><title>To-Do Lists</title></html>'''

def home_page( request):
    return HttpResponse( hpHTML)