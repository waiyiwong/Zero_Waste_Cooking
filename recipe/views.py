from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_recipe(request):
    return HttpResponse("Hello, recipe!")