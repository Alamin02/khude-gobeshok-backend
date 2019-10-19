from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from comments.serializers import CommentSerializer
from comments.models import Comment


# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = Comment.objects.all()
        project = self.request.query_params.get('project', None)
        if project is not None:
            queryset = queryset.filter(project=project)
        return queryset

    def get_serializer_context(self):
        return {'user': self.request.user}
