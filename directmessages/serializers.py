from rest_framework import serializers
from .models import DirectMessage


class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DirectMessage
        fields = ['sender', 'recipient', 'content', 'sent_at']


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = ['sender', 'recipient', 'content']
