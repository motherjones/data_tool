from django.db import models

class Subscribers(models.Model):
    email = models.CharField(max_length=40)
    email_domain = models.CharField(max_length=24)
    active = models.BooleanField()
    date = models.DateField()
    bounces = models.IntegerField()
