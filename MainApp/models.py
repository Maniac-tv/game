from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

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
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    runtime = models.IntegerField()
    invisible = models.BooleanField(default=False)

class Game(models.Model):
    game_id = models.TextField(max_length=20, db_index=True)
    game_name = models.TextField(max_length=50)
    description = models.TextField(max_length=5000)
    inventory = models.TextField(max_length=500)
    pointers = models.TextField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    invisible = models.BooleanField(default=False)
# Create your models here.
