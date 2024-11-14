from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=60) # bcrypt hash
    created_at = models.DateTimeField(auto_now_add=True)

class HealthData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.BooleanField()
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    health_history = models.TextField()
