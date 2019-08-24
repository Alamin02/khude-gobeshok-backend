from rest_framework.serializers import ModelSerializer, CharField
from .models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'start_date', 'end_date', 'description']


class ProjectListSerializer(ModelSerializer):
    author = CharField(source='author.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'thumbnail', 'created_at', 'author']
