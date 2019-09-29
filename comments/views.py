from django.shortcuts import render
from rest_framework import viewsets
from comments.serializers import CommentSerializer
from comments.models import Comment


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
