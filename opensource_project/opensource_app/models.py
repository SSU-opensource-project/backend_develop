from django.db import models

# Create your models here.

class User_info(models.Model):
    email_addr = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    gender = models.BooleanField()

