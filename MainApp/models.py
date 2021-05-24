from django.db import models
from datetime import datetime

class Form (models.Model):
    pointer_id = models.TextField(max_length=20, db_index=True)
    name_location = models.TextField(max_length=50)
    lat = models.FloatField(max_length=25)
    long = models.FloatField(max_length=25)
    description = models.TextField(max_length=255)
    help = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    area = models.TextField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

# Create your models here.
