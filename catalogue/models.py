from django.db import models


# Create your models here.
class Catalouge(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    img = models.ImageField
    status = models.CharField
