from django.contrib import admin
from .models import Object, Subject ,rdf_type, Ontology
# Register your models here.








@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    pass







admin.site.register(Subject)
admin.site.register(rdf_type)
admin.site.register(Ontology)

# Register your models here.

