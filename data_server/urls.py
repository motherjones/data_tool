from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^admin/', include(admin.site.urls)),
)
