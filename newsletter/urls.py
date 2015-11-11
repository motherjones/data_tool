from django.conf.urls import url

from newsletter import views

urlpatterns = [
    url(r'^subscribers-upload$', views.UploadSubscribersView.as_view(),
        name='subscribers-upload'),
    url(r'^query-upload$', views.UploadQueryView.as_view(),
        name='query-upload'),
    url(r'^subscribers-report/(?P<pk>\d+)/', views.ActiveSubscribersView.as_view(), name='subscribers-report'),
    url(r'^subscribers-report/', views.WeekListView.as_view(), name='subscribers-report-list'),
    url(r'^signups-report/', views.SignupsReportView.as_view(), name='signups-report'),
    url(r'^longevity-report/', views.LongevityReportView.as_view(), name='longevity-report'),
    url(r'^churn-report/', views.ChurnReportView.as_view(), name='churn-report'),
    url(r'^$', views.IndexPage.as_view(), name='newsletter-index'),
]
