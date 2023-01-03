from django.urls import path
from .views import ProjectList, ProjectDetail, TaskList, TaskDetail

urlpatterns = [
    path('project/', ProjectList.as_view()),
    path('project/<int:pk>', ProjectDetail.as_view()),
    path('task/', TaskList.as_view()),
    path('task/<int:pk>', TaskDetail.as_view()),
]
