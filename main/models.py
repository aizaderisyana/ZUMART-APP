from django.db import models
 

class Product(models.Model):
    name = models.CharField(max_length=255, default="default_value")
    kelas = models.CharField(max_length=255,  default="default_value")
    description = models.TextField()
    appName = models.CharField(max_length=255,  default="default_value")
    amount = models.IntegerField()