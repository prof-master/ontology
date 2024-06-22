from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import os



def index(request):
    template  = render_to_string("ontology_auth/index.html")
    return HttpResponse(template)

<<<<<<< HEAD
def auth(request):
    template  = render_to_string("ontology_auth/auth.html")
    return HttpResponse(template)




# Create your views here.
=======
>>>>>>> ae9bf83b2e7c08717ddd6e79164d38e11785c4ea
