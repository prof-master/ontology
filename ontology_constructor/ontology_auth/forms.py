from django import ModelForm
from .models import Object, Subject ,rdf_type, Ontology

class Ontologyform(ModelForm):
    class Meta:
        model = Ontology
        fields = ['name', 'description']
