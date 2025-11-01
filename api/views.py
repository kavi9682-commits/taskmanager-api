from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner= self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all
    serializer_class = RegisterSerializer
    permission_classes= []