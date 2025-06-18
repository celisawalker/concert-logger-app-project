from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
class Concert(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('Event Date')
    venue = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    seat = models.CharField(max_length=20)
    review = models.TextField(blank=True, null=True)
    image = CloudinaryField("image")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('concert-detail', kwargs={'concert_id': self.id})


class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    top_five = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Library(models.Model):
    description = models.CharField(max_length=250, blank=True, null=True)
    image = CloudinaryField("image")

    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.description)
    
    # def get_absolute_url(self):
    #     return reverse('concert-detail', kwargs={'library_id': self.id})