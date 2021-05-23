from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from mysite.views import add, welcome, login, index, logout, register, HereView
from restaurants.views import menu, list_restaurants, comment

#from django.contrib.auth import views as auth_views
# below is django default login logout method (default login, logout uses login.html under mysite/templates/registration)
#from django.contrib.auth.views import login, logout

urlpatterns = patterns(
    '',
    # mysite
    #url(r'^here/$', here),
    url(r'^here/$', HereView.as_view()),
    url(r'^admin/', include(admin.site.urls))
)

urlpatterns += patterns(
    # restaurants
    url(r'^(\d{1,2})/plus/(\d{1,2})/$', add),
    url(r'^menu/$', menu),
    url(r'^welcome/$', welcome),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^comment/(\d{1,5})/$', comment),
    #url(r'^accounts/', include('django.contrib.auth.urls')), # login
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^index/$', index),
    url(r'^accounts/register/$', register)
    )
