from django.db import models


# Create your models here.

class Course(models.Model):
    id_course = models.CharField(primary_key=True, max_length=999)
    name_course = models.CharField(max_length=255)
    img_course = models.ImageField(upload_to='course/%Y/%m/%d/')
    description = models.TextField(max_length=5000)
    status = models.CharField(max_length=10)
    pl_course = models.CharField(max_length=255)
    objects_course = models.CharField(max_length=255)
    target = models.TextField(max_length=5000)
    gv = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)

    def __str__(self):
        return self.name_course

