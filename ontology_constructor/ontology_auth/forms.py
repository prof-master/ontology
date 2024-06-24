from django import forms
from django.forms import ModelForm
from .models import Object, Subject ,rdf_type, Ontology

class OntologyForm(ModelForm):
    class Meta:
        model = Ontology
        fields = ['name', 'access']
    def __init__(self, *args, **kwargs):
        super(OntologyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': '.ipt_wrapper', "size": "80", "required": True})
        self.fields['access'].widget.attrs.update({"length": "40", "required": True})
        #self.fields['name'].widget.attrs.update("size": "40")
        
class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'description']
    def __init__(self, *args, **kwargs):
        super(SubjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': '.ipt_wrapper', "size": "80", "required": True})
        self.fields['description'].widget.attrs.update({"size": "80", "width": "40", "required": True})
        #self.fields['name'].widget.attrs.update("size": "40")