from users.models import User
from .models import Project
from .serializers import ProjectSerializer, ProjectListSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView


# Create your views here.
class Create(CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class List(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer


class Retrieve(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# View for user's own project list
class ProfileProjectList(ListAPIView):
    serializer_class = ProjectListSerializer
    lookup_url_kwarg = "profile_username"

    def get_queryset(self):
        profile_name = self.kwargs.get(self.lookup_url_kwarg)
        user = User.objects.get(username=profile_name)

        # Have to add exception when user not found
        return Project.objects.filter(author=user)
