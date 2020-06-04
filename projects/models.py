from django.db import models

# Create your models here.


class projects(models.Model):
    jobtitle = models.CharField(max_length=20)
    jobtype = models.CharField(max_length=20)
    paymentmethod = models.CharField(max_length=20)
    jobdescription = models.CharField(max_length=200)

    class Meta:
        db_table = "projects"


class user():
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=20,primary_key=True)
    location = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    gmail = models.CharField(max_length=20)
    twlink = models.CharField(max_length=20)
    fblink = models.CharField(max_length=20)
    gitlink = models.CharField(max_length=20)


    def __str__(self):
        return self.jobtitle
