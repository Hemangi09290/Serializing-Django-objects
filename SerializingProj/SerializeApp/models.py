from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    
