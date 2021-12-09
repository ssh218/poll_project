from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    active_until=models.DateTimeField(auto_now=True)
    status= models.DateTimeField(auto_now=True)