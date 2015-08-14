from django.contrib import admin

from newsletter import models


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('signup', 'active', 'bounces',)
    raw_id_fields = ("signup",)


class SignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'created',)
    raw_id_fields = ("email",)


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'email_domain')


admin.site.register(models.Subscriber, SubscriberAdmin)
admin.site.register(models.Week)
admin.site.register(models.Signup, SignupAdmin)
admin.site.register(models.Email)

