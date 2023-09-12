from django.db import models
 

class Product(models.Model):
    name = models.CharField(max_length=255)
    kelas = models.CharField(max_length=255)
    description = models.TextField()
    appName = models.CharField(max_length=255)
    amount = models.IntegerField()