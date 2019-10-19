from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, DestroyAPIView, \
    RetrieveAPIView, UpdateAPIView
from rest_framework import viewsets, mixins
from users.models import User, Education, Job
from users.serializers import UserSerializer, ProfileSerializer, \
    EducationListSerializer, EducationSerializer, JobSerializer, \
    ProfileBioSerializer, ProfileSpecializedInSerializer, \
    ProfileSoftwareSkillSerializer, SquadSerializer, UpdateProfilePicSerializer


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class RetrieveUser(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = "profile_username"

    def get_object(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        user = User.objects.get(username=profile_name)
        return user


class RetrieveProfile(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    lookup_url_kwarg = "profile_username"

    def get_object(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        profile = User.objects.get(username=profile_name).profile
        return profile


class UpdateBio(UpdateAPIView):
    serializer_class = ProfileBioSerializer

    def get_object(self):
        profile = User.objects.get(username=self.request.user).profile
        return profile


class UpdateProfilePic(UpdateAPIView):
    serializer_class = UpdateProfilePicSerializer

    def get_object(self):
        profile = User.objects.get(username=self.request.user).profile
        return profile


class UpdateSpecializedIn(UpdateAPIView):
    serializer_class = ProfileSpecializedInSerializer
    lookup_url_kwarg = "profile_name"

    def get_object(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        profile = User.objects.get(username=profile_name).profile
        return profile


class UpdateSoftwareSkill(UpdateAPIView):
    serializer_class = ProfileSoftwareSkillSerializer
    lookup_url_kwarg = "profile_name"

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


# Have to add authentication
class CreateEducation(CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Have to add authentication
class DeleteEducation(DestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ListJob(ListAPIView):
    serializer_class = JobSerializer
    lookup_url_kwarg = "profile_username"

    def get_queryset(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        user = User.objects.get(username=profile_name)
        return Job.objects.filter(user=user)


# Have to add authentication
class CreateJob(CreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Have to add authentication
class DeleteJob(DestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class SquadViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = SquadSerializer
    queryset = User.objects.all()
