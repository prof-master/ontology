from django.db import models
<<<<<<< HEAD

=======
from django.utils import timezone
from django.contrib.auth.models import User
>>>>>>> ae9bf83b2e7c08717ddd6e79164d38e11785c4ea
# Create your models here.
class Ontology(models.Model):
    ACCESS_CHOICES=[
        ('Global', 'Общедоступная'),
        ('Private', 'Приватная'),
        ]
    name=models.CharField(max_length=100)
    access=models.CharField(
        max_length=50,
        choices=ACCESS_CHOICES,
        default='Global',
        )
    craeted_at=models.DateTimeField(default=timezone.now)
    owner=models.ForeignKey(
        User,
        related_name='ontology',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
        )
    

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uri
class Object(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uri
class rdf_type(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
<<<<<<< HEAD
=======
    subject=models.ForeignKey(
        Subject,
        related_name='subject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True

    )
    object_ont=models.ForeignKey(
        Object,
        related_name='object_ont',
        on_delete=models.SET_NULL,
        null=True,
        blank=True

    )
    ontology=models.ForeignKey(
        Object,
        related_name='ontology',
        on_delete=models.CASCADE

    )
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
>>>>>>> ae9bf83b2e7c08717ddd6e79164d38e11785c4ea
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uri
