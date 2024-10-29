from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:M:S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
 
class Employee(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    models.ImageField( upload_to=getFileName, height_field=None, width_field=None, max_length=None)
    class Meta:
        db_table="User"
    
    def __str__(self):
        return self.name