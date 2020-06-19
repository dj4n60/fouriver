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
    location = models.CharField(max_length=22, default="not available")
    language = models.CharField(max_length=22, default="not available")
    github = models.CharField(max_length=50, default="not available")
    cv = models.CharField(max_length=50, default="not available")
    profile_pic = models.ImageField(upload_to='static/images/', )

    class Meta:
        db_table = "developerinfo"


class customerinfo(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=22, default="not available")
    disc = models.CharField(max_length=150, default="not available")
    linkedin = models.CharField(max_length=50, default='not available')
    profile_pic = models.ImageField(upload_to='static/images/')

    class Meta:
        db_table = "customerinfo"

