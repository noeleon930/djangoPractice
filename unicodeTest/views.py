from django.shortcuts import render
from django.http import HttpResponse

def helloUrl(request, name):
    return HttpResponse("Hello there, " + name)
