from django.contrib import admin

from newsletter import models

class SubscriberAdmin(admin.ModelAdmin):
    raw_id_fields = ("email",)

class SignupAdmin(admin.ModelAdmin):
    raw_id_fields = ("email",)

admin.site.register(models.Subscriber, SubscriberAdmin)
admin.site.register(models.Week)
admin.site.register(models.Signup, SignupAdmin)
admin.site.register(models.Email)

