from django.contrib import admin
from .models import Object, Subject ,rdf_type, Ontology
# Register your models here.


#@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    pass




class rdf_typeInLine(admin.TabularInline):
    model=rdf_type
    extra=0
    fields=('name', 'subject', 'object', 'created_at',)
    can_delete=True
    show_change_link=True
@admin.register(Ontology)
class OntologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'access', 'created_at', 'owner')
    search_fields = ('name', 'created_at', 'owner')
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    inlines=[rdf_typeInLine]
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    #ordering = ('created_at')
    #date_hierarchy = 'created_at'
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    ordering = ('created_at',)
    date_hierarchy = 'created_at'
    

@admin.register(rdf_type)
class rdf_typeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'subject', 'object', 'ontology')
    search_fields = ('name',)
    ordering = ('ontology', 'created_at')
    date_hierarchy = 'created_at'
    
#admin.site.register(Ontology)
#admin.site.register(Subject)
#admin.site.register(Object)
#admin.site.register(rdf_type)


# Register your models here.

