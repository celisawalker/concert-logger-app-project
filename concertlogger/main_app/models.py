from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Concert(models.Model):
    artist_name = models.CharField(max_length=100)
    date = models.DateField('Event Date')
    venue = models.CharField(max_length=100)
    seat = models.CharField(max_length=20)


    