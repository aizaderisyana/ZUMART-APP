from django.db import models
from django.contrib.auth.models import User

class Items(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField(default=1000000)  
    size = models.IntegerField(default=38)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
