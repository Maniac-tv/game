from django.db import models

class Form (models.Model):
    pointer_id = models.TextField(max_length=20)
    name_location = models.TextField(max_length=50)
    lat = models.FloatField(max_length=25)
    lang = models.FloatField(max_length=25)
    description = models.TextField(max_length=255)
    help = models.TextField(max_length=255)
    area = models.TextField(max_length=20)

# Create your models here.
