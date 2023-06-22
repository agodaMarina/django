from django.db import models
from django.utils import timezone


# Create your models here.

class Categorie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Articles(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    auteur = models.CharField(max_length=250)
    image = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=200)
    isPublish = models.BooleanField()
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
