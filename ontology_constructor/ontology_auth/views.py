from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
def index(request):
    template  = render_to_string("ontology_auth/index.html")
    return HttpResponse(template)

<<<<<<< HEAD
=======
# Create your views here.
>>>>>>> d84fc231c4ab9c5f43e7945b1be574f564a7b5da
