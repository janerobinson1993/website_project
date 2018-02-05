from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    paragraph_one = models.CharField(max_length=10000)
    paragraph_two = models.CharField(max_length=10000)
    paragraph_three = models.CharField(max_length=10000)
    #add image here
    teaser_image = models.ImageField(upload_to='images')
    title_image = models.ImageField(upload_to='images')
