from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request ,*args , **kwargs):
    ## the example of the simple use of httpresponse
    # return HttpResponse("<h1>hellp world</h1>")

    return render(request , 'home.html' , {})