import pytz
from datetime import datetime, time, timedelta

from django.db import models
from django.db.models import Q, Count

from django.utils.http import urlencode


class Email(models.Model):
    email = models.CharField(unique=True, db_index=True, max_length=100)
    email_domain = models.CharField(db_index=True, max_length=100)


class Signup(models.Model):
    email = models.ForeignKey('Email', db_index=True)
    code = models.CharField(db_index=True, max_length=200)
    created = models.DateTimeField(db_index=True)
    signup_url = models.URLField(max_length=400, db_index=True)
    group = models.CharField(db_index=True, max_length=200)


class Week(models.Model):
    date = models.DateField(unique=True)
    complete = models.BooleanField(default=False)

    @classmethod
    def get_latest(cls):
        qs = cls.objects.order_by('-date')
        return qs[0]

    def subscribers_count(self):
        return self.subscriber_set.all().count()

    def inactive_subscribers(self):
        return self.subscriber_set.filter(Q(active=False) | Q(bounces__gt=1))

    def inactive_subscribers_count(self):
        return self.inactive_subscribers().count()

    def active_subscribers(self):
        return self.subscriber_set.filter(active=True).filter(bounces__lte=1)

    def active_subscribers_count(self):
        return self.active_subscribers().count()

    def previous_week(self):
        pre = self.get_previous_by_date()
        return pre

    def change_in_subscribers(self):
        pre = self.previous_week()
        return self.subscribers_count() - pre.subscribers_count()

    def change_in_active_subscribers(self):
        pre = self.previous_week()
        return self.active_subscribers_count() - pre.active_subscribers_count()

    def new_subscribers(self):
        subs = Subscriber.objects.filter(signup__in=self.new_signups())
        return subs

    def active_new_subscribers(self):
        return self.new_subscribers().filter(active=True).filter(bounces__lte=1)

    def inactive_new_subscribers(self):
        return self.new_subscribers().filter(Q(active=False) | Q(bounces__gt=1))

    def active_to_inactive(self):
        current_inactive = self.inactive_subscribers().values('signup')
        change = self.previous_week().active_subscribers().filter(signup__in=current_inactive)
        return change.count()

    def inactive_to_active(self):
        current_active = self.active_subscribers().values('signup')
        change = self.previous_week().inactive_subscribers().filter(signup__in=current_active)
        return change.count()

    @property
    def end_date(self):
        t = time(10,0)
        end = datetime.combine(self.date, t)
        tz = pytz.timezone('US/Pacific')
        return tz.localize(end)

    @property
    def start_date(self):
        return self.end_date - timedelta(days=7)

    def new_signups(self):
        n = Signup.objects.filter(created__gt=self.start_date).filter(created__lte=self.end_date)
        return n

    def signups_report(self):
        dformat = '%Y-%m-%d'
        q = {
            'start_date': self.start_date.strftime(dformat),
            'end_date': self.end_date.strftime(dformat),
            'report_type': 'svg',
        }
        return urlencode(q)

    def __unicode__(self):
        return self.date


class Subscriber(models.Model):
    signup = models.ForeignKey('Signup', db_index=True)
    active = models.NullBooleanField(db_index=True)
    week = models.ForeignKey('Week', db_index=True)
    bounces = models.IntegerField(db_index=True)
    updated_on = models.DateTimeField()
