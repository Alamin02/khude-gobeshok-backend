from django.shortcuts import render
from rest_framework import viewsets
from .models import DirectMessage
from .serializers import ConversationSerializer
from django.db.models import Q


class ConversationViewSet(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        ret = DirectMessage.objects.latest_distinct()
        ret = ret.filter(Q(sender=self.request.user)| Q(recipient=self.request.user))
        return ret
