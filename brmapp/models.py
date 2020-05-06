from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)

    

