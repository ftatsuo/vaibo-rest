from django.db import models

# Create your models here.
class Smartphone(models.Model):
  product = models.CharField(max_length=50)
  brand = models.CharField(max_length=50)
  vaibo_score = models.IntegerField()