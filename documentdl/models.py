from django.db import models


# Create your models here.

class DocumentDL(models.Model):
    id_dl = models.CharField(primary_key=True, max_length=255)
    name_cus = models.CharField
    phone_cus = models.ImageField
    email_cus = models.EmailField
    link = models.CharField

