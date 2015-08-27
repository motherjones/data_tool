import pytz
from datetime import datetime, time, timedelta

from django.db import models
from django.db.models import Q, Count

from django.utils.http import urlencode


class Email(models.Model):
    email = models.CharField(unique=True, db_index=True, max_length=100)
    email_domain = models.CharField(db_index=True, max_length=100)

    def __str__(self):
        return self.email


class SignupQuerySet(models.QuerySet):
    def first(self):
        return self.filter(is_first=True)


class Signup(models.Model):
    email = models.ForeignKey('Email', db_index=True)
    code = models.CharField(db_index=True, max_length=200)
    created = models.DateTimeField(db_index=True)
    signup_url = models.URLField(max_length=400, db_index=True)
    group = models.CharField(db_index=True, max_length=200)
    is_first = models.BooleanField(db_index=True, default=True)
    objects = SignupQuerySet.as_manager()


class Week(models.Model):
    date = models.DateField(db_index=True,unique=True)
    notes = models.TextField(default='')
    complete = models.BooleanField(default=False)

    #Aggregate values
    net_active_change = models.IntegerField(null=True)
    new_emails_count = models.IntegerField(null=True)
    active_to_inactive_count = models.IntegerField(null=True)
    inactive_to_active_count = models.IntegerField(null=True)
    new_active = models.IntegerField(null=True)

    def update_aggregate(self):
        if self.previous_week():
            self.net_active_change = self.change_in_active_subscribers()
            self.new_emails_count = self.new_emails().count()
            self.active_to_inactive_count = self.active_to_inactive()
            self.inactive_to_active_count = self.inactive_to_active()
            self.new_active = self.active_new_subscribers().count()
            self.save()

    @classmethod
    def get_latest(cls):
        qs = cls.objects.order_by('-date')
        return qs[0]

    def subscribers_count(self):
        return self.subscriber_set.first().count()

    def inactive_subscribers(self):
        return self.subscriber_set.first().filter(Q(active=False) | Q(bounces__gt=1))

    def inactive_subscribers_count(self):
        return self.inactive_subscribers().count()

    def active_subscribers(self):
        return self.subscriber_set.first().filter(active=True).filter(bounces__lte=1)

    def active_subscribers_count(self):
        return self.active_subscribers().count()

    def previous_week(self):
        try:
            pre = self.get_previous_by_date()
        except self.DoesNotExist:
            return None
        return pre

    def change_in_subscribers(self):
        pre = self.previous_week()
        return self.subscribers_count() - pre.subscribers_count()

    def change_in_active_subscribers(self):
        pre = self.previous_week()
        return self.active_subscribers_count() - pre.active_subscribers_count()

    def new_subscribers(self):
        subs = self.subscriber_set.first().filter(signup__in=self.new_signups())
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
        n = Signup.objects.first().filter(created__gt=self.start_date).filter(created__lte=self.end_date)
        return n

    def new_emails(self):
        old = self.previous_week().subscriber_set.first().values('signup')
        new = self.subscriber_set.first().exclude(signup__in=old)
        return new

    def signups_report(self):
        dformat = '%Y-%m-%d'
        q = {
            'start_date': self.start_date.strftime(dformat),
            'end_date': self.end_date.strftime(dformat),
            'report_type': 'svg',
        }
        return urlencode(q)

    def __str__(self):
        return u"%s" % self.date


class SubscriberQuerySet(models.QuerySet):
    def first(self):
        return self.filter(signup__is_first=True)


class Subscriber(models.Model):
    signup = models.ForeignKey('Signup', db_index=True)
    active = models.NullBooleanField(db_index=True)
    week = models.ForeignKey('Week', db_index=True)
    bounces = models.IntegerField(db_index=True)
    updated_on = models.DateTimeField()
    objects = SubscriberQuerySet.as_manager()
