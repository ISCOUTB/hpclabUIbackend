from ..serializers import PublicToolSerializer
from ..models import Tool
from ..imports import *


class WorkflowToolsView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    @staticmethod
    def get(request):
        tools = Tool.objects.filter(public=True)
        serializer = PublicToolSerializer(tools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def put(self, request, format=None):
    #     request.data['creator'] = request.user.id
    #     serializer = FileSerializer(data=request.data)
    #     if not serializer.is_valid():
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     else:
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)