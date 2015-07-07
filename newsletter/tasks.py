from __future__ import absolute_import

import csv

from celery import shared_task
from newsletter import models

@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param

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
            subscriber = models.Subscriber()
            try:
                subscriber.week = week
                subscriber.bounces = line[0]
                subscriber.email = line[1]
                subscriber.active = truthy.get(line[2])
                subscriber.domain = line[3]
                subscriber.save()
            except:
                print(line)
        week.complete = True
        week.save()
