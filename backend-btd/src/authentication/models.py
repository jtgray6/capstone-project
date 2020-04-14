from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    fav_color = models.CharField(blank=True, max_length=120)

class Brewery(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    website_url = models.TextField()
    logo_url = models.TextField()
    image_url = models.TextField()

    def __str__(self):
        return self.name

class Beer(models.Model):
    name = models.CharField(max_length=255)
    style = models.CharField(max_length=255)
    rating = models.FloatField()
    abv = models.FloatField()
    description = models.TextField()
    release_date = models.DateField()
    image_url = models.TextField()
    brewery = models.ForeignKey(Brewery, related_name="beers", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
