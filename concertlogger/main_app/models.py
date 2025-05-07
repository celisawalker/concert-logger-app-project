from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Concert(models.Model):
    artist_name = models.CharField(max_length=100)
    date = models.DateField('Event Date')
    venue = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    seat = models.CharField(max_length=20)
    review = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    top_five = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    