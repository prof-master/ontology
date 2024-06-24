"""
URL configuration for ontology_constructor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from ontology_auth.views import index,auth,profile, constructor, add_ontology
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('auth/',auth,name='auth'),
    path('profile/',profile,name='profile'),
    path('constructor/',constructor,name='constructor'),
    path('ontology/new', add_ontology, name='add_ontology'),
    path('accounts/', include('django.contrib.auth.urls')),
        
]
