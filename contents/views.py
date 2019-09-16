from rest_framework.generics import CreateAPIView
from contents.models import ImageContent, ThumbnailImage, ProfileImage
from contents.serializers import ImageContentSerializer, ThumbnailImageSerializer, ProfileImageSerializer


class Create(CreateAPIView):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer


class ThumbnailCreate(CreateAPIView):
    queryset = ThumbnailImage.objects.all()
    serializer_class = ThumbnailImageSerializer


class ProfilePicUpload(CreateAPIView):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
