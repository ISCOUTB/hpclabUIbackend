__author__ = 'juan'
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #return obj.creator == request.user
        if obj.creator == request.user:
            return True
        else:
            raise Http404
