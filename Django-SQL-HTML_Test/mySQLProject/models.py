from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    id = models.BigAutoField(primary_key=True)

class Animal(models.Model):
    legs = models.CharField(max_length=255)
    type = models.IntegerField()
    id = models.BigAutoField(primary_key=True)

