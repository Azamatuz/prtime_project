from django.db import models

# Create your models here.
class Day(models.Model):
    day_start = models.DateField()
    day_end = models.DateField()
