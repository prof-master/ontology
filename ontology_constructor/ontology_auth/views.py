from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import os



def index(request):
    template  = render_to_string("ontology_auth/index.html")
    return HttpResponse(template)

def auth(request):
    template  = render_to_string("ontology_auth/auth.html")
    return HttpResponse(template)

def profile(request):
    template  = render_to_string("ontology_auth/profile.html")
    return HttpResponse(template)

def constructor(request):
    template  = render_to_string("ontology_auth/constructor.html")
    return HttpResponse(template)

# Create your views here.
