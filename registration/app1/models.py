from django.db import models

# Create your models here.
class Book_ground(models.Model):
    bid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    mobile = models.CharField(max_length=10)