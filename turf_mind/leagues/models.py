from django.db import models

# Create your models here.

# leagues/models.py


class Club(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    deep = models.IntegerField()
    deep_allowed = models.IntegerField()
    draws = models.IntegerField()
    h_a = models.CharField(max_length=1)  
    loses = models.IntegerField()
    missed = models.IntegerField()
    npxg = models.DecimalField(max_digits=10, decimal_places=3)
    npxga = models.DecimalField(max_digits=10, decimal_places=3)
    npxgd = models.DecimalField(max_digits=10, decimal_places=3)
    ppda = models.JSONField()  
    ppda_allowed = models.JSONField()  
    pts = models.IntegerField()
    result = models.CharField(max_length=1) 
    scored = models.IntegerField()
    wins = models.IntegerField()
    xg = models.DecimalField(max_digits=10, decimal_places=3)
    xga = models.DecimalField(max_digits=10, decimal_places=3)
    xpts = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name
