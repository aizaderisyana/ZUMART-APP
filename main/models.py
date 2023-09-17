from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField(default=1000000)  
    size = models.IntegerField(default=38)
