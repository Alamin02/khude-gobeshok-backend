from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer, ProjectListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView


# Create your views here.
class Create(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class List(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class Retrieve(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
