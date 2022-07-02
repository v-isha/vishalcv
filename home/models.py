from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=100)
    remark = models.TextField(max_length=1000)
