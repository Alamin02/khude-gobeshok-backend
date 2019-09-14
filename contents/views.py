from rest_framework.generics import CreateAPIView
from contents.models import ImageContent, ThumbnailImage
from contents.serializers import ImageContentSerializer, ThumbnailImageReadSerializer


class Create(CreateAPIView):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer


class ThumbnailCreate(CreateAPIView):
    queryset = ThumbnailImage.objects.all()
    serializer_class = ThumbnailImageReadSerializer

