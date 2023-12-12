from django.db import models

# Create your models here.

class Club(models.Model):
    date = models.DateTimeField()
    deep = models.IntegerField()
    deep_allowed = models.IntegerField()
    draws = models.IntegerField()
    h_a = models.CharField(max_length=1)
    loses = models.IntegerField()
    missed = models.IntegerField()
    npxg = models.FloatField()
    npxga = models.FloatField()
    npxgd = models.FloatField()
    ppda = models.JSONField()
    ppda_allowed = models.JSONField()
    pts = models.IntegerField()
    result = models.CharField(max_length=1)
    scored = models.IntegerField()
    wins = models.IntegerField()
    xg = models.FloatField()
    xga = models.FloatField()
    xpts = models.FloatField()

    class Meta:
          managed = False 
