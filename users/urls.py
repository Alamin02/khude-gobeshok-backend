from django.urls import path

from users.views import GetUser

urlpatterns = [
    path('get-user/', GetUser.as_view(), name="get_user"),
]
