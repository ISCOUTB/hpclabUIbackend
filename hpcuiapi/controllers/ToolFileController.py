from ..serializers import ToolFileSerializer
from ..models import ToolFile
from ..imports import *
from rest_framework.decorators import permission_classes
from rest_framework.parsers import FormParser, MultiPartParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class ToolFilesView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    parser_classes = (MultiPartParser, FormParser)

    @staticmethod
    def get(request, tk):
        files = ToolFile.objects.filter(tool=tk)
        serializer = ToolFileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    @permission_classes(IsAdminUser,)
    def put(request, tk):
        serializer = ToolFileSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ToolFilesDetail(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_object(self, tk, fk):
        try:
            tool_file = ToolFile.objects.get(pk=fk)
            self.check_object_permissions(self.request, tool_file)
            return tool_file
        except ToolFile.DoesNotExist:
            raise Http404

    @permission_classes(IsAdminUser,)
    def get(self, request, tk, fk):
        tool_file = self.get_object(tk, fk)
        serializer = ToolFileSerializer(tool_file)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes(IsAdminUser,)
    def delete(self, request, tk, fk):
        tool_file = self.get_object(tk, fk)
        tool_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)