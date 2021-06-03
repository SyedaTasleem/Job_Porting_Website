from django import forms
from django.db import models

# Create your models here.

class JobDetail(models.Model):
  jobtitle = models.CharField(max_length=200)
  jobdescription = models.TextField()


    #favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))

#class insertJobs(models.Model):
 # job = models.CharField( max_length=100)
   