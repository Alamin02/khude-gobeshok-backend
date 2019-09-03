from django.urls import path
from .views import Create, List, Retrieve, ProfileProjectList


urlpatterns = [
    path('create/', Create.as_view(), name='project_create'),
    path('list/', List.as_view(), name='project_list'),
    path('retrieve/<pk>/', Retrieve.as_view(), name='project_retrieve'),
    path('list/<str:profile_username>', ProfileProjectList.as_view(), name="profile_project_list"),
]
