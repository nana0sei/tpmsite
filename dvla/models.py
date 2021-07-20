from django.db import models


# Create your models here.
class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    age = models.IntegerField()
    nationality = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

