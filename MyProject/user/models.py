from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=40)
    Mobile=models.CharField(max_length=30)
    Message=HTMLField()
    def __str__(self):
        return self.Name
######################################################################
class slider(models.Model):
    shead=models.CharField(max_length=300)
    ssubject=models.CharField(max_length=300)
    sdes=HTMLField()
    spic=models.ImageField(upload_to='static/slider/',default="")
    def __str__(self):
        return self.shead
######################################################################
class igallery(models.Model):
    gname=models.CharField(max_length=400)
    gpic=models.ImageField(upload_to='static/gallery/',default="")
    def __str__(self):
        return self.gname
######################################################################

class ncategory(models.Model):
    category=models.CharField(max_length=80)
    cpic=models.ImageField(upload_to='static/categroy',null=True)
    cdate=models.DateField()
    def __str__(self):
        return self.category
#######################################################################

class city(models.Model):
    ncity=models.CharField(max_length=30)
    cpic=models.ImageField(upload_to='static/city',null=True)
    cdate=models.DateField()
    def __str__(self):
        return self.ncity
#######################################################################
class mynews(models.Model):
    ntitle=models.CharField(max_length=500)
    nhead=models.CharField(max_length=500)
    ndes=HTMLField()
    npic=models.ImageField(upload_to='static/news/',null=True)
    ncity=models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(ncategory,on_delete=models.CASCADE,null=True)
    ndate=models.DateField()
#######################################################################
class videonews(models.Model):
    vlink=models.CharField(max_length=200)
    vhead=models.CharField(max_length=500)
    vcategory=models.ForeignKey(ncategory,on_delete=models.CASCADE,null=True)
    vcity=models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    vdate=models.DateField()
    vdes=HTMLField()

#######################################################################