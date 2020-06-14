from django.db import models
from django import forms

# Create your models here.


class projects(models.Model):
    jobtitle = models.CharField(max_length=20)
    jobtype = models.CharField(max_length=20)
    paymentmethod = models.CharField(max_length=20)
    jobdescription = models.CharField(max_length=200)
    #taggeddev = models.CharField(max_length=200)


    class Meta:
        db_table = "projects"


class user():
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    gmail = models.CharField(max_length=20)
    twlink = models.CharField(max_length=20)
    fblink = models.CharField(max_length=20)
    gitlink = models.CharField(max_length=20)


    def __str__(self):
        return self.jobtitle


class developerinfo(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=22)
    language = models.CharField(max_length=22)
    github = models.CharField(max_length=50)
    cv = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='static/images/profile_pics/', height_field=500, width_field=500, max_length=100)

    class Meta:
        db_table = "devinfo"


class customerinfo(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=22, )
    disc = models.CharField(max_length=150, )
    linkedin = models.CharField(max_length=50, )
    profile_pic = models.ImageField(upload_to='static/images/profile_pics/', height_field=500, width_field=500, max_length=100)

    class Meta:
        db_table = "customerinfo"

