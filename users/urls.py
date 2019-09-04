from django.urls import path

from users.views import GetUser, RetrieveProfile

urlpatterns = [
    path('get-user/', GetUser.as_view(), name="get_user"),
    path('profile/<str:profile_username>', RetrieveProfile.as_view(), name="get_profile"),
]
