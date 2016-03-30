from ..serializers import FileSerializer
from ..models import File
from ..imports import *
from rest_framework.parsers import FormParser, MultiPartParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class FilesView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, pk):
        files = File.objects.filter(creator=request.user.id, project=pk)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        request.data['creator'] = request.user.id
        serializer = FileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class FileDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    def get_object(self, fk):
        try:
            fileobject = File.objects.get(pk=fk)
            self.check_object_permissions(self.request, fileobject)
            return fileobject
        except File.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        fileobject = self.get_object(fk)
        serializer = FileSerializer(fileobject)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, fk):
        fileobject = self.get_object(fk)
        fileobject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
