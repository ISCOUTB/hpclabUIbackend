from ..serializers import PublicToolSerializer, TaskSerializer
from ..models import Tool, Task
from ..imports import *


class WorkflowToolsView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        tools = Tool.objects.filter(public=True)
        serializer = PublicToolSerializer(tools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TasksView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request, pk):
        tasks = Task.objects.filter(project=pk)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskView(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_object(self, tk, uuid):
        try:
            task = Task.objects.filter(uuid=uuid)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404


    def put(self, request, pk, uuid):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, uuid):
        taskobject = self.get_object(pk, uuid)
        taskobject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
