import random
import os
from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.


class Blogposts(models.Model):
    backimage=models.ImageField(null=True,blank=False,upload_to='images')
    bodytitle= models.CharField(max_length=100)
    blogauthor=models.CharField(max_length=50)
    blogbody=models.TextField()

    def __str__(self):
        return self.bodytitle

    def __unicode__(self):
        return self.bodytitle

