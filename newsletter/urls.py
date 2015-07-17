from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^subscribers-upload$', views.UploadSubscribersView.as_view(),
        name='subscribers_upload'),
    url(r'^subscribers-report/(?P<pk>\d+)/', views.ActiveSubscribersView.as_view(), name='subscribers-report'),
    url(r'^subscribers-report/', views.WeekListView.as_view(), name='subscribers-report-list'),
    url(r'^signups-report/', views.SignupsReportView.as_view(), name='signups-report'),
]
