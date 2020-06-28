from django.db import models
from django import forms
from auth.models import appusers

# Create your models here.


class projects(models.Model):
    jobtitle = models.CharField(max_length=20)
    jobtype = models.CharField(max_length=20)
    paymentmethod = models.CharField(max_length=20)
    jobdescription = models.CharField(max_length=200)
    category = models.CharField(max_length=50, null=True)
    privacy = models.CharField(max_length=20,null=True)
    tagdev = models.CharField(max_length=100,null=True)
    offerby = models.CharField(max_length=100,null=True)
    createdby = models.CharField(max_length=100,null=True)
    isCompleted = models.BooleanField(default=False) #feveloper
    isCompletedbyDeveloper = models.BooleanField(default=False) #o dev accepted
    isCopletedbyClient = models.BooleanField(default=False) # okay meta to ratign ginetai true
    developercomments = models.CharField(max_length=100,null=True)



class Meta:
    db_table = "projects"

    def __str__(self):
        return self.jobtitle


class user():
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=20, primary_key=True)
    location = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    gmail = models.CharField(max_length=20)
    twlink = models.CharField(max_length=20)
    fblink = models.CharField(max_length=20)
    gitlink = models.CharField(max_length=20)


class offers(models.Model):
    developername = models.CharField(max_length=100,null=True)
    projectid = models.IntegerField()
    projecttitle = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    money = models.IntegerField()
    isAccepted = models.BooleanField(default=False)

    class Meta:
        db_table = "offers"

        def __str__(self):
            return self.developername

class reccomends(models.Model):
    developername = models.CharField(max_length=100,null=True)
    projectid = models.CharField(max_length=100,null=True)
    projecttitle = models.CharField(max_length=100,null=True)
    reccomendedby = models.CharField(max_length=100,null=True)


    class Meta:
        db_table = "reccomends"

    def __str__(self):
        return self.developername

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

class comments(models.Model):
    commentby = models.CharField(max_length=100)
    projectid = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)

    class Meta:
        db_table = "comments"
