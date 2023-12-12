from django.db import models

# Create your models here.

class Player(models.Model):
    league = models.CharField(max_length=255)
    matches = models.CharField(max_length=255)
    mp = models.IntegerField()
    per_90_minutes_ast = models.FloatField()
    per_90_minutes_g_a = models.FloatField()
    per_90_minutes_g_a_pk = models.FloatField()
    per_90_minutes_g_pk = models.FloatField()
    per_90_minutes_gls = models.FloatField()
    performance_ast = models.FloatField()
    performance_crdr = models.FloatField()
    performance_crdy = models.FloatField()
    performance_g_a = models.FloatField()
    performance_g_pk = models.FloatField()
    performance_gls = models.FloatField()
    performance_pk = models.FloatField()
    performance_pkatt = models.FloatField()
    player = models.CharField(max_length=255)
    player_age = models.IntegerField()
    player_nation = models.CharField(max_length=255)
    player_position = models.CharField(max_length=255)
    playing_time_90s = models.FloatField()
    playing_time_min = models.IntegerField()
    playing_time_mp = models.IntegerField()
    playing_time_starts = models.IntegerField()
    progression_prgc = models.FloatField()
    progression_prgp = models.FloatField()
    progression_prgr = models.FloatField()
    season = models.CharField(max_length=255)
    team = models.CharField(max_length=255)

    class Meta:
          managed = False 
