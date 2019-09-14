from rest_framework.serializers import ModelSerializer, ImageField
from .models import ImageContent, ThumbnailImage


class ImageContentSerializer(ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ['image']


class ThumbnailImageCreateSerializer(ModelSerializer):
    class Meta:
        model = ThumbnailImage
        fields = ['image']


class ThumbnailImageReadSerializer(ModelSerializer):
    thumbnail = ImageField('thumbnail', )

    class Meta:
        model = ThumbnailImage
        read_only = ('thumbnail')
        fields = ['image', 'thumbnail']
