from rest_framework import serializers
from .models import Project, User
from contents.serializers import ThumbnailImageSerializer


class ProjectCreateSerializer(serializers.ModelSerializer):
    author = serializers.CharField(max_length=150)
    cover_image_obj = ThumbnailImageSerializer(read_only=True, source='cover_image')

    class Meta:
        model = Project
        fields = [
            'title',
            'author',
            'tags',
            'teammates',
            'cover_image',
            'cover_image_obj',
            'start_date',
            'end_date',
            'description'
        ]

    def create(self, validated_data):
        data = validated_data.copy()

        # TODO: Add exception e.g: get_object_or_404
        data['author'] = User.objects.get(username=data['author'])
        return super(ProjectCreateSerializer, self).create(data)


class ProjectListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username')
    cover_image = ThumbnailImageSerializer()

    class Meta:
        model = Project
        fields = ['id', 'title', 'cover_image', 'created_at', 'author']
