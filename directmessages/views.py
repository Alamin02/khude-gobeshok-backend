from django.shortcuts import render
from rest_framework import viewsets
from .models import DirectMessage
from users.models import User
from .serializers import ConversationSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        profile_name = self.request.GET.get('username', None)
        if profile_name is not None:
            contact = User.objects.get(username=profile_name)
            ret = DirectMessage.objects.filter((Q(sender=self.request.user) & Q(recipient=contact)) | (Q(sender=contact) & Q(recipient=self.request.user)))
        else:
            ret = DirectMessage.objects.latest_distinct()
            ret = ret.filter(Q(sender=self.request.user) | Q(recipient=self.request.user))
        return ret
