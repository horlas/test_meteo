from django.db import models

# Create your models here.


class Peak(models.Model):
    name = models.CharField("Peak name", max_length=150)
    lat = models.IntegerField()
    lon = models.IntegerField()
    altitude = models.IntegerField()
