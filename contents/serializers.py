from rest_framework.serializers import ModelSerializer, ImageField
from .models import ImageContent, ThumbnailImage2


class ImageContentSerializer(ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ['image', 'caption']


class ThumbnailImageCreateSerializer(ModelSerializer):
    class Meta:
        model = ThumbnailImage2
        fields = ['image']


class ThumbnailImageReadSerializer(ModelSerializer):
    thumbnail = ImageField('thumbnail', )

    class Meta:
        model = ThumbnailImage2
        read_only = ('thumbnail')
        fields = ['image', 'thumbnail']
