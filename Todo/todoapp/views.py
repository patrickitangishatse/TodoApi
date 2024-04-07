from django.shortcuts import render
from .models import Task
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TaskSerializer
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend




# Create your views here.
@extend_schema(tags=['tasks'])
class TaskListCreate(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'completed','due_date']
    search_fields=['title','description']



@extend_schema(tags=['Task Update and Delete'])
class TaskRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field='id'