from rest_framework.serializers import ModelSerializer, ImageField
from .models import ImageContent, ThumbnailImage, ProfileImage


class ImageContentSerializer(ModelSerializer):
    class Meta:
        model = ImageContent
        fields = ['image']


class ThumbnailImageSerializer(ModelSerializer):
    thumbnail = ImageField('thumbnail', )

    class Meta:
        model = ThumbnailImage
        read_only = 'thumbnail'
        fields = ['id', 'image', 'thumbnail']


class ProfileImageSerializer(ModelSerializer):
    thumbnail = ImageField('thumbnail', )

    class Meta:
        model = ProfileImage
        read_only = 'thumbnail'
        fields = ['id', 'image', 'thumbnail']

