from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.views import AppList, AppDetail
urlpatterns = patterns('',
    url(r'^$', AppList.as_view(), name='applist'),
    url(r'^(?P<slug>[-\w]+)/$', AppDetail.as_view(), name='app'),
)