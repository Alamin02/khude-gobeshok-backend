from django.urls import path
from .views import ProfileProjectList


urlpatterns = [
    path('list/<str:profile_username>', ProfileProjectList.as_view(), name="profile_project_list"),
]
