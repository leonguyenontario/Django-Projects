from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=100)
    url = models.TextField(max_length=300)
    ima = models.ImageField(upload_to = 'hinh/',default = '')

class

class Projects(models.Model):
    name = models.CharField(max_length=100,blank=True)
    desciption = models.TextField(max_length=500,blank=True)
    imageGalery = models.ForeignKey()