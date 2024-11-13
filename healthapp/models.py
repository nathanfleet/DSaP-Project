from django.db import models

class HealthData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.BooleanField()
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    health_history = models.TextField()
