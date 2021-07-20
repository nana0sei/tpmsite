from django.db import models


# Create your models here.
class Individual(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
