from django.db import models
import uuid

# Create your models here.
class ScoreBoard(models.Model):
    playerid = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150)
    score = models.IntegerField(default=0)
    IsLevelFinished = models.BooleanField(default=False)
    IsGameFinished = models.BooleanField(default=False)