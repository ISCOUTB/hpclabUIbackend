from django.conf.urls import patterns, include, url
from django.contrib import admin
from hpcuiapi.controllers import FileController, ProjectController, UserController, ToolController
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
                       url(r'^api-token-verify/', 'rest_framework_jwt.views.verify_jwt_token'),
                       url(r'^projects/$', ProjectController.ProjectsView.as_view()),
                       url(r'^projects/(?P<pk>[0-9]+)/$', ProjectController.ProjectDetail.as_view()),
                       url(r'^files/$', FileController.FilesView.as_view()),
                       url(r'^files/(?P<fk>[0-9]+)/$', FileController.FileDetail.as_view()),
                       url(r'^user/', UserController.UserView.as_view()),
                       url(r'^tools/', ToolController.ToolsView.as_view()),
                       url(r'^tools/(?P<fk>[0-9]+)/$', ToolController.ToolDetail.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
