from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import OntologyForm
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

def add_ontology(request):
    if request.method == 'POST':
        form = OntologyForm(request.POST)
        #product = ShoppingItem(name=product.name, list=shopping_list, price=product.price, product=product)
        product.save()
        return HttpResponse('updated')
    
# Create your views here.
