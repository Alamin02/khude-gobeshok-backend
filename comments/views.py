from django.shortcuts import render
from rest_framework import viewsets
from comments.serializers import CommentSerialzer
from comments.models import Comment


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerialzer
    queryset = Comment.objects.all()
