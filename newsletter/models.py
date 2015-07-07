from functools import wraps
from django.db import models
from django.db.models import Q


def memoize(func):
    @wraps(func)
    def memoizer(*args, **kwargs):
        if not hasattr(func, '_cache'):
            func._cache = func(*args, **kwargs)
        return func._cache
    return memoizer


class Week(models.Model):
    date = models.DateField(unique=True)
    complete = models.BooleanField(default=False)

    @memoize
    def subscribers_count(self):
        return self.subscriber_set.all().count()

    @memoize
    def inactive_subscribers(self):
        return self.subscriber_set.filter(active=True).filter(bounces__lte=1)

    @memoize
    def inactive_subscribers_count(self):
        return self.inactive_subscribers().count()

    @memoize
    def active_subscribers(self):
        return self.subscriber_set.filter(active=True).filter(bounces__lte=1)

    @memoize
    def active_subscribers_count(self):
        return self.active_subscribers().count()


class Subscriber(models.Model):
    email = models.CharField(max_length=40)
    email_domain = models.CharField(max_length=24)
    active = models.BooleanField()
    week = models.ForeignKey('Week')
    bounces = models.IntegerField()


