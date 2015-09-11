from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from hpcuiapi.serializers import ProjectSerializer
from django_auth_ldap.backend import LDAPBackend
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated
from hpcuiapi.models import Project
from django.http import Http404
from hpcuiapi.permissions import IsOwner
from rest_framework.authentication import TokenAuthentication
#
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

class ProjectsView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        projects = Project.objects.filter(creator=request.user.id)
        projectsSerializer = ProjectSerializer(projects, many=True)
        return Response(projectsSerializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        projectSerializer = ProjectSerializer(data=request.data)
        if not projectSerializer.is_valid():
            return Response(projectSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data = projectSerializer.data
            creator = request.user
            newProject = Project(creator=creator, name=data['name'], description=data['description'])
            newProject.save()
            request.data['id'] = newProject.pk
            return Response(request.data, status=status.HTTP_201_CREATED)


class ProjectDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner, )

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        projectDetailSerializer = ProjectSerializer(project)
        return Response(projectDetailSerializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        projectDetailSerializer = ProjectSerializer(project, data=request.data)
        if projectDetailSerializer.is_valid():
            projectDetailSerializer.save()
            return Response(projectDetailSerializer.data, status=status.HTTP_200_OK)
        return Response(projectDetailSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
