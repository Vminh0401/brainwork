from django.db import models


# Create your models here.

class Infofeedback(models.Model):
    name_info = models.CharField
    dvct = models.CharField(max_length=255)
    phone_number = models.IntegerField
    email_info = models.EmailField
    y_c = models.CharField


