from rest_framework import viewsets,permissions,status
from .serializers import TaskSerializer,TaskCreateSerializer
from .models import Tasks
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import CustomUser

class TaskViewset(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_classes = {
        "list":TaskSerializer,
        "create":TaskCreateSerializer,
        "retrive":TaskSerializer,
        "update":TaskSerializer,
        "partial_update":TaskSerializer
    }
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes[self.action]

    def get_queryset(self):
        return Tasks.objects.filter(user = self.request.user)
    
    

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context
    

    @action(detail=False, methods=['get'])
    def get_task_stat_count(self,request):
        response_dict = {}
        completed_task_count = Tasks.objects.filter(status=Tasks.COMPLETED,user=self.request.user).count()
        pending_task_count = Tasks.objects.filter(status=Tasks.PENDING,user=self.request.user).count()
        in_progress_count = Tasks.objects.filter(status=Tasks.IN_PROGRESS,user=self.request.user).count()

        response_dict["completed_task"] = completed_task_count
        response_dict["pending_task"] = pending_task_count
        response_dict["in_progress"] = in_progress_count

        return Response(response_dict,status=status.HTTP_200_OK)



