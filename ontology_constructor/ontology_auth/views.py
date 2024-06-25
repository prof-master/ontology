from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import OntologyForm, SubjectForm, ObjectForm, rdf_typeForm
from .models import Ontology, Subject, Object, rdf_type
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

def ontology_list_1(request):
    ontologys= Ontology.objects.all()
    context= {'ontologys': ontologys}
    return render(request, "ontology_auth/ontology_list.html", context)
    
def ontology_detail(request, ontology_id):
    ontology_cur= get_object_or_404(Ontology, id=ontology_id)
    rdf_types=rdf_type.objects.filter(ontology=ontology_cur)
    context= {'rdf_types': rdf_types, 'ontology': ontology_cur}
    return render(request, "ontology_auth/ontology_detail.html", context)
   
def add_ontology(request):
    if request.method == 'POST':
        form = OntologyForm(request.POST)
        if form.is_valid():
            form.save('ontology')
            form=OntologyForm()
            return redirect('/ontology/list')
    else:
        form=OntologyForm()
        return render(request, 'ontology_auth/add_ontology.html', {'form': form})

def add_subject(request):
    if request.method == 'POST':
        form_sub = SubjectForm(request.POST)
        if form_sub.is_valid():
            form_sub.save('subject')
            form_sub = SubjectForm()
            return redirect('/ontology/list')
    else:
        form_sub=SubjectForm()
        return render(request, 'ontology_auth/add_subject.html', {'form': form_sub})

def add_object(request):
    if request.method == 'POST':
        form_sub = ObjectForm(request.POST)
        if form_sub.is_valid():
            form_sub.save('object')
            form_sub = ObjectForm()
            return redirect('/ontology/list')
    else:
        form_sub=ObjectForm()
        return render(request, 'ontology_auth/add_object.html', {'form': form_sub})
    
def add_rdf_type(request):
    if request.method == 'POST':
        form_sub = rdf_typeForm(request.POST)
        if form_sub.is_valid():
            form_sub.save('rdf_type')
            form_sub = rdf_typeForm()
            return redirect('/ontology/list')
    else:
        form_sub=rdf_typeForm()
        return render(request, 'ontology_auth/add_rdf_type.html', {'form': form_sub})
# Create your views here.
