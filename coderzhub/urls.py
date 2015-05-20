from django.conf.urls import patterns, include, url
from django.contrib.auth.views import logout
from django.contrib import admin
admin.autodiscover()

from hubusers.views import *
from siteforms.views import *
from projects.views import *
from search.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^messages/', include('django_messages.urls')),
    url(r'^$', FrontPage, name='home'),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^addproject/', Project_Form), #navigate here through the dashboard?
    url(r'^search_tabs/$',tabs),
    url(r'^search_tabs/(?P<error>[A-Za-z0-9]+)/$',tabs),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('search.urls')),
    url(r'^about_us/$', about_us_page),
    url(r'^', include('hubusers.urls')),
    url(r'^activity/', include('actstream.urls')),
)
