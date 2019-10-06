from rest_framework import serializers
from .models import DirectMessage


class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DirectMessage
        fields = ['sender', 'recipient', 'content', 'sent_at', 'sender_name', 'recipient_name']

    sender_name = serializers.SerializerMethodField('get_sender_name')
    recipient_name = serializers.SerializerMethodField('get_recipient_name')

    def get_sender_name(self, obj):
        return obj.sender.username

    def get_recipient_name(self, obj):
        return obj.recipient.username


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = ['sender', 'recipient', 'content']
