from django.db import models
from django.utils import timezone

# Create your models here.
class Articles (models.Model):

    titre = models.CharField(max_length=200)
    description = models.TextField()
    auteur=models.CharField(max_length=250)
    image=models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    tags=models.CharField(max_length=200)
    isPublish=models.BooleanField()

    

    
