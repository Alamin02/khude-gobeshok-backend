from rest_framework import serializers
from .models import Project, User


class ProjectCreateSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=150)

    class Meta:
        model = Project
        fields = ['title', 'author', 'tags', 'teammates', 'thumbnail', 'start_date', 'end_date', 'description']

    def create(self, validated_data):
        data = validated_data.copy()

        # TODO: Add exception e.g: get_object_or_404
        data['author'] = User.objects.get(username=data['author'])
        return super(ProjectCreateSerializer, self).create(data)


class ProjectListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')

    class Meta:
        model = Project
        fields = ['id', 'title', 'thumbnail', 'created_at', 'author']
