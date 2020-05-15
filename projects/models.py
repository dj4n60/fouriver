from django.db import models

# Create your models here.


class projects(models.Model):
    jobtitle = models.CharField(max_length=20)
    jobtype = models.CharField(max_length=20)
    paymentmethod = models.CharField(max_length=20)
    jobdescription = models.CharField(max_length=100)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.jobtitle
