from django.contrib import admin
from django.conf.urls import patterns, include, url

from django.conf.urls.defaults import *
from sites.ex_systime import current_datetime
from sites.ex_systime import hours_ahead
from sites.ex_systime import m_current_datetime
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    (r'^mtime/$', m_current_datetime),
    (r'^admin/', include(admin.site.urls)),
    #(r'^admin/', include('django.contrib.admin.urls')),
    # Examples:
    # url(r'^$', 'sites.views.home', name='home'),
    # url(r'^sites/', include('sites.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
