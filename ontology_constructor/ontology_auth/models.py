<<<<<<< HEAD
from django.db import models

# Create your models here.
class Subject(models.Model):
    name=models.CharField()
    uri=models.CharFied()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uri
class Object(models.Model):
    name=models.CharField()
    uri=models.CharFied()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uri
class rdf_type(models.Model):
    name=models.CharField()
    uri=models.CharFied()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.uri
=======
from django.db import models

# Create your models here.
>>>>>>> 3959197b9392de9167a19270e55166effc7736b7