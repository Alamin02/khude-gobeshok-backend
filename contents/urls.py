from django.urls import path
from contents.views import Create, ThumbnailCreate, ThumbnailList

urlpatterns = [
    path('image-add', Create.as_view(), name="image_add"),
    path('thumbnail-add', ThumbnailCreate.as_view(), name="thumbnail_add"),
    path('thumbnail-list', ThumbnailList.as_view(), name="thumbnail_list"),
]
