from rest_framework import generics
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

# Create your views here.
class ProjectList(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        queryset = Task.objects.all()
        project =  self.request.query_params.get('project')
        if project is not None:
            queryset = queryset.filter(project = project)
        return queryset


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


