from django.db import models

# Create your models here.
class Subject(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uri
class Object(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uri
class rdf_type(models.Model):
<<<<<<< HEAD
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
=======
    subject=models.ForeignKey(
        Subject,
        related_name='subject',
        on_delete=models.CASCADE

    )
    object=models.ForeignKey(
        Object,
        related_name='object',
        on_delete=models.CASCADE

    )
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uri
