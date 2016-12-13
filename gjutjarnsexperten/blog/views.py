from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'blog/index.html')


#from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
#from django.urls import reverse

#from .models import Question, Choice
