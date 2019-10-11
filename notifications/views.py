from django.shortcuts import render
from rest_framework import viewsets, mixins
from .serializers import NotificationSerializer
from .models import Notification


class NotificationViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        ret = Notification.objects.filter(recipient=self.request.user)
        return ret
