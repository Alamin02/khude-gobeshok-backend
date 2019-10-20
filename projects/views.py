from users.models import User
from .models import Project
from .serializers import ProjectCreateSerializer, ProjectListSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound


class ProjectViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        else:
            return ProjectCreateSerializer

    def get_queryset(self):
        profile_name = self.request.GET.get('username', None)
        if profile_name is not None:
            try:
                user = User.objects.get(username=profile_name)
            except ObjectDoesNotExist:
                raise NotFound
            return Project.objects.filter(author=user)
        else:
            return Project.objects.all()
