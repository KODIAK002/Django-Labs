from django.db import models

# Create your models here.
from django.db import models

class Location(models.Model):
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
