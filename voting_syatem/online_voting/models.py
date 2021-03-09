from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.
class user_info(models.Model):
    username = models.CharField(max_length=20)
    emailid = models.CharField(max_length=40)
    password = models.CharField(max_length=20)
