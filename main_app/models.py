from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    players = models.CharField(max_length=100)
    playtime = models.CharField(max_length=100)
    description = models.TextField(max_length=300)