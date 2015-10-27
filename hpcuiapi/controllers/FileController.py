from ..serializers import FileSerializer
from ..models import File
from ..imports import *
from rest_framework.parsers import FileUploadParser, JSONParser, FormParser, MultiPartParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class FilesView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)
    # parser_classes = (FileUploadParser, )
    # parser_classes = (JSONParser, )
    # parser_classes = (FormParser, )
    parser_classes = (MultiPartParser, FormParser)

    @staticmethod
    def get(request):
        files = File.objects.filter(creator=request.user.id)
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        request.data['creator'] = request.user.id
        serializer = FileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # datafile = self.request.data.get('file')
        # file = request.data
        # return Response(file.encode('utf-8'))


class FileDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, IsOwner,)

    def get_object(self, fk):
        try:
            fileobject = File.objects.get(pk=fk)
            self.check_object_permissions(self.request, fileobject)
            fileobject.size = fileobject.file.size
            return fileobject
        except File.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        fileobject = self.get_object(fk)
        serializer = FileSerializer(fileobject)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, fk):
    #     fileobject = self.get_object(fk)
    #     serializer = FileSerializer(fileobject, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fk):
        fileobject = self.get_object(fk)
        fileobject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
