from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hopefully this will show on the startpage?")

