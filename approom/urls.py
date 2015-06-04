from django.conf.urls import include, url
from django.contrib import admin
from approom.views import HomePageView

urlpatterns = [
    # Examples:
    url(r'^$', HomePageView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^apps/', include('apps.urls')),
    url(r"^account/", include("account.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
