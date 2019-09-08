from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView

from users.models import User, Education, Job
from users.serializers import UserSerializer, ProfileSerializer, EducationListSerializer, EducationSerializer, JobSerializer


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


class ListEducation(ListAPIView):
    serializer_class = EducationListSerializer
    lookup_url_kwarg = "profile_username"

    def get_queryset(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        user = User.objects.get(username=profile_name)
        return Education.objects.filter(user=user)


class CreateEducation(CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ListJob(ListAPIView):
    serializer_class = JobSerializer
    lookup_url_kwarg = "profile_username"

    def get_queryset(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        user = User.objects.get(username=profile_name)
        return Job.objects.filter(user=user)


class CreateJob(CreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
