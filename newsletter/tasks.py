from __future__ import absolute_import

import csv

from pytz import timezone
from datetime import datetime
from celery import shared_task
from newsletter import models

@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param

def convio_datetime_to_datetime(date):
    ctz = timezone('US/Central')
    (date, time) = date.split(' ')
    (month, day, year) = date.split('/')
    (hour, minute) = time.split(':')
    year = 2000 + int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)
    return datetime(year=year, month=month, day=day, hour=hour, minute=minute, tzinfo=ctz)


@shared_task
def load_active_subscribers(path, date):
    with open(path, 'r') as csv_file:
        records = csv.reader(csv_file)
        records.__next__()
        truthy = { 'true': True, 'false' : False }
        week = models.Week()
        week.date = date
        week.save()
        for line in records:
            created_on = convio_datetime_to_datetime(line[2])
            modified_on = convio_datetime_to_datetime(line[4])
            (signup, created) = models.Signup.objects.get_or_create(email=line[1],
                defaults={
                    'code': line[0],
                    'created': created_on,
                    'signup_url': line[3],
                    'email_domain': line[7],
                })
            subscriber = models.Subscriber()
            subscriber.week = week
            subscriber.bounces = line[6]
            subscriber.signup = signup
            subscriber.updated_on = modified_on
            subscriber.active = truthy.get(line[5])
            subscriber.save()
        week.complete = True
        week.save()
