from django.urls import path
from contents.views import Create, ThumbnailCreate, ProfilePicUpload

urlpatterns = [
    path('images', Create.as_view()),
    path('thumbnails', ThumbnailCreate.as_view()),
    path('propics', ProfilePicUpload.as_view()),
]
