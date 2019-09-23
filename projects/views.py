from users.models import User
from .models import Project
from .serializers import ProjectCreateSerializer, ProjectListSerializer
from rest_framework.generics import ListAPIView
from rest_framework import viewsets, mixins


class ProjectViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        else:
            return ProjectCreateSerializer

# View for user's own project list
class ProfileProjectList(ListAPIView):
    serializer_class = ProjectListSerializer
    lookup_url_kwarg = "profile_username"

    def get_queryset(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        user = User.objects.get(username=profile_name)

        # Have to add exception when user not found
        return Project.objects.filter(author=user)
