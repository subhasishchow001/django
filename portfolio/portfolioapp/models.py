import random
import os
from django.db import models

# Create your models here.
def filename_ext(filepath):
    base_name= os.path.basename(filepath)
    name, ext=os.path.splitext(base_name)
    return name,ext


def upload_path(instance,filename):
    newfilename=random.randint(1,36771586)
    name, ext = filename_ext(filename)
    final_name='{final_name}{ext}'.format(new_name=newfilename,ext=ext)
    return "{new_name}/{final_name}".format(new_name=newfilename,final_name=final_name)


class Blogposts(models.Model):
    backimage=models.ImageField(upload_to=upload_path,null=True,blank=False)
    bodytitle= models.CharField(max_length=100)
    blogauthor=models.CharField(max_length=50)
    blogbody=models.TextField()

    def __str__(self):
        return self.bodytitle

    def __unicode__(self):
        return self.bodytitle
