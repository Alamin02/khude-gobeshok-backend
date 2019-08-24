from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView

from contents.models import ImageContent, ThumbnailImage2
from contents.serializers import ImageContentSerializer, ThumbnailImageCreateSerializer, ThumbnailImageReadSerializer


class Create(CreateAPIView):
    queryset = ImageContent.objects.all()
    serializer_class = ImageContentSerializer


class ThumbnailCreate(CreateAPIView):
    queryset = ThumbnailImage2.objects.all()
    serializer_class = ThumbnailImageReadSerializer


class ThumbnailList(ListAPIView):
    queryset = ThumbnailImage2.objects.all()
    serializer_class = ThumbnailImageReadSerializer
