from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from apps.views import AppList
urlpatterns = patterns('',
    url(r'^$', AppList.as_view(), name='applist'),
)