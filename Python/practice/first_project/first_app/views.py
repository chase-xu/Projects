from django.shortcuts import render
from django.http import HttpResponse   ##import httpresponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am from views.py !"} ##content of the page
    return render(request, 'first_app/index.html', context=my_dict)