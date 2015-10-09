__author__ = 'juan'
from ..serializers import UserSerializer
from ..models import User
from ..imports import *
from django.shortcuts import get_object_or_404


class UserView(APIView):
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    @staticmethod
    def get(request):
        user = get_object_or_404(User, pk=request.user.id)
        user = UserSerializer(user)
        return Response(user.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request):
        user = get_object_or_404(User, pk=request.user.id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
