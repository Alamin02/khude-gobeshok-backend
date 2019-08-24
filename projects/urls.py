from django.urls import path
from .views import Create, List, Retrieve


urlpatterns = [
    path('create/', Create.as_view(), name='project_create'),
    path('list/', List.as_view(), name='project_list'),
    path('retrieve/<pk>/', Retrieve.as_view(), name='project_retrieve'),
]
