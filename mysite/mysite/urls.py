from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite.views import here, add

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here/$', here),
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', add)
)
