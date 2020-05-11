from django.db import models

# Create your models here. databases models


class Users(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    idiotita = models.CharField(max_length=1)
