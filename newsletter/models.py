from django.db import models

class Week(models.Model):
    date = models.DateField(unique=True)
    complete = models.BooleanField(default=False)

class Subscriber(models.Model):
    email = models.CharField(max_length=40)
    email_domain = models.CharField(max_length=24)
    active = models.BooleanField()
    week = models.ForeignKey('Week')
    bounces = models.IntegerField()


