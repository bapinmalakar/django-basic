from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def page2Home(request):
    return HttpResponse('Welcome to page 2');
