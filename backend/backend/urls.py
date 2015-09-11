from django.conf.urls import patterns, include, url
from django.contrib import admin
from hpcuiapi import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^api-token-auth/', views.ObtainAuthToken.as_view()),
                       url(r'^projects/$', views.ProjectsView.as_view()),
                       url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectDetail.as_view())
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
