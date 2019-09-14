from django.urls import path
from contents.views import Create, ThumbnailCreate

urlpatterns = [
    path('image-add', Create.as_view(), name="image_add"),
    path('thumbnail-add', ThumbnailCreate.as_view(), name="thumbnail_add"),
]
