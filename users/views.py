from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView

from users.models import Profile, User
from users.serializers import UserSerializer, ProfileSerializer


class GetUser(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class RetrieveProfile(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_url_kwarg = "profile_username"

    def get_object(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        profile = User.objects.get(username=profile_name).profile
        return profile
