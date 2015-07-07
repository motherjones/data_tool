from django.contrib import admin

from newsletter import models

admin.site.register(models.Subscriber)
admin.site.register(models.Week)

