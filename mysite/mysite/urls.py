from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from mysite.views import here, add, welcome #, menu
from restaurants.views import menu, list_restaurants, comment

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    # mysite
    url(r'^here/$', here),
    # restaurants
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', add),
    url(r'^menu/(\d{1,5})/$', menu),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^accounts/', include('django.contrib.auth.urls')), # login
)
