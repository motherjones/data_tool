from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subscribers-upload$', views.UploadSubscribersView.as_view(),
        name='subscribers_upload'),
    url(r'^subscribers-report/(?P<pk>\d+)/', views.ActiveSubscribersView.as_view(), name='subscribers-report'),
]
