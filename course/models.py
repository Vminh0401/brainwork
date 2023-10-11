from django.db import models


# Create your models here.

class Course(models.Model):
    id_course = models.CharField(primary_key=True, max_length=255)
    name_course = models.CharField(max_length=255)
    img_course = models.ImageField
    description = models.CharField(max_length=255)
    status = models.CharField
    pl_course = models.CharField
    objects_course = models.CharField(max_length=255)
    target = models.CharField
    gv = models.CharField(max_length=50)
    content = models.CharField

