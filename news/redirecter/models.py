from django.db import models

# Create your models here.
from django.db import models 
from datetime import datetime

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=150)
    imgLink = models.CharField(max_length=150)
    isForAdults = models.BooleanField(default=False)
    isForeignNews = models.BooleanField(default=False)
    isPoliticalNews = models.BooleanField(default=False)
    tags = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.title