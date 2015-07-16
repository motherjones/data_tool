from __future__ import absolute_import

import csv

from pytz import timezone
from datetime import datetime
from celery import shared_task
from newsletter import models

@shared_task
def test(param):
    print('test')
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

def build_code_grouper():
    group_dict = {
        'Bottom of Article' : ['MJ_artbot3',],
        'ICN confirmation page links': ['icn_20130404', 'MJ_icn_donor', 'MJ_icn', 'mj_icn', 'ICN_0910_import'],
        'TOC unpubbed articles': ['MJ_toc'],
        'RH grey widget': ['MJ_swr'],
        'Mobile devices': ['MJ_mob', 'MJ_mob_overlay'],
        'Colorful RH widgets': ['MJ_RHtopv1', 'MJ_RHTopEco', 'MJ_RHTopDrum'],
        'Postage stamp': ['MJ_postagev1',],
        #'Collapsible top-of-site box': [],
        'Change.org/ Care2.org': ['care2', 'change_dot_org', 'change_dot_org_all', 'MJ_Care2_all_newsletters', 'care2_mojo_petition', 'Care2_Petition2012'],
        'Overlay widget': ['MJ_overlay', 'mj_overlay', 'MJ_newsletter_overlay'],
        'House ads': ['MJ_houseads', 'MJ_embed_billboard','MJ_newsletter_scroller'],
        'Google Ad Words': ['MJ_1209google',],
        'Follow Box': ['MJ_followbox',],
        'Bottom bar': ['mj_bottom_bar',],
        'Other house links': ['mj_detroit_survey', 'MJ_nlpg2', 'MJ_newsletter_redirect'],
        'Other/special': ['', 'primary_tracker', 'unknown','redrocks','mj_alternet', 'Administrative Add',     'administrative add'],
        'Facebook Page': ['MJ_facebook'],
        'Unclassified': ['dccc_survey', 'MJ_MXpromo0512', 'client', 'MJ_1209grist', 'MJ_swt', 'MJ_mrpg', 'MJ_swl', 'MJ_icn', 'MJ_swtp', 'MJ_four', 'MJ_jopg', 'MJ_hepg', 'admin_test_ignore', 'MJ_clco', 'MJ_home', 'mj_RHtopv1', 'MJ_artpage', 'MJ_mbmr'],
    } 
    groups = group_dict.keys()
    swapped_group_dict = {}
    grouped_affiliate_bins = {}
    for group, codes in group_dict.items():
        for code in codes:
            swapped_group_dict[code] = group
    def getter(code):
        try:
            return swapped_group_dict[code]
        except:
            return code
    return getter

@shared_task
def load_active_subscribers(path, date):
    with open(path, 'r') as csv_file:
        records = csv.reader(csv_file)
        records.__next__()
        truthy = { 'true': True, 'false' : False }
        (week, creaded_week) = models.Week.objects.get_or_create(date=date)
        code_grouper = build_code_grouper()
        for line in records:
            if len(line) == 8:
                created_on = convio_datetime_to_datetime(line[2])
                modified_on = convio_datetime_to_datetime(line[4])
                group = code_grouper(line[0])
                try:
                    (signup, created) = models.Signup.objects.get_or_create(email=line[1],
                        defaults={
                            'code': line[0],
                            'created': created_on,
                            'signup_url': line[3],
                            'email_domain': line[7],
                            'group': group,
                        })
                except:
                    print(line)
                else:
                    subscriber = models.Subscriber()
                    subscriber.week = week
                    subscriber.bounces = line[6]
                    subscriber.signup = signup
                    subscriber.updated_on = modified_on
                    subscriber.active = truthy.get(line[5])
                    try:
                        subscriber.save()
                    except:
                        print(line)
            else:
                print(line)
        week.complete = True
        week.save()
