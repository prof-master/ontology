from django.shortcuts import render, redirect
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
        if form.is_valid():
            form.save('ontology')
            template  = render_to_string("ontology_auth/constructor.html")
            return HttpResponse(template)
    else:
        form=OntologyForm()
        #template  = render_to_string("ontology_auth/add_ontology.html")
        return render(request, 'ontology_auth/add_ontology.html', {'form': form})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save('subject')
            template  = render_to_string("ontology_auth/constructor.html")
            return HttpResponse(template)
    else:
        form=SubjectForm()
        #template  = render_to_string("ontology_auth/add_ontology.html")
        return render(request, 'ontology_auth/constructor.html', {'form': form_sub})


# Create your views here.
