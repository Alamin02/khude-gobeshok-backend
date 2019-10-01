from django.shortcuts import render
from rest_framework import viewsets
from comments.serializers import CommentSerializer
from comments.models import Comment


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        project = self.request.query_params.get('project', None)
        if project is not None:
            queryset = queryset.filter(project=project)
        return queryset
