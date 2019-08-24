from django.shortcuts import render
from django.http import HttpResponse   ##import httpresponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World") ##content of the page