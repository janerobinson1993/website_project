from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    body_text = models.CharField(max_length=10000)
    #add image here

