from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationSerializer
from .models import Notification


class NotificationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        ret = Notification.objects.filter(recipient=self.request.user)
        return ret
