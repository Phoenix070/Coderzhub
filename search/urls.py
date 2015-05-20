from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns('',
    url(r'^domain/(?P<language>[A-Za-z0-9_-]+)/$',search_by_domain),
    url(r'^user/(?P<username>[A-Za-z0-9]+)/$',search_by_user),
    url(r'^status/(?P<status>[A-Za-z0-9]+)/$',search_by_status),
    url(r'^project/(?P<project_name>[A-Za-z0-9_-]+)/$',search_by_project),
)