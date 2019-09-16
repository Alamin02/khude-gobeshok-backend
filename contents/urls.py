from django.urls import path
from contents.views import Create, ThumbnailCreate, ProfilePicUpload

urlpatterns = [
    path('image-add', Create.as_view(), name="image_add"),
    path('thumbnail-add', ThumbnailCreate.as_view(), name="thumbnail_add"),
    path('propic-add', ProfilePicUpload.as_view(), name="propic_add"),
]
