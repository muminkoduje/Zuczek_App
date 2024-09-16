from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=10,unique=True)
    host =models.CharField(max_length=5,unique=True)
    guest_can_pause = models.BooleanField(null=False,default=False)
  

