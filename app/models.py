from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    email=models.EmailField()
    person=models.IntegerField()
    date=models.DateField()