from rest_framework import serializers
from .models import DirectMessage
from users.models import User


class ConversationSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(max_length=150)
    recipient = serializers.CharField(max_length=150)

    class Meta:
        model = DirectMessage
        fields = ['sender', 'recipient', 'content', 'sent_at', 'sender_name', 'recipient_name']

    sender_name = serializers.SerializerMethodField('get_sender_name')
    recipient_name = serializers.SerializerMethodField('get_recipient_name')

    def get_sender_name(self, obj):
        return obj.sender.username

    def get_recipient_name(self, obj):
        return obj.recipient.username

    def create(self, validated_data):
        data = validated_data.copy()

        # TODO: Add exception e.g: get_object_or_404
        data['sender'] = User.objects.get(username=data['sender'])
        data['recipient'] = User.objects.get(username=data['recipient'])
        return super(ConversationSerializer, self).create(data)


class DirectMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectMessage
        fields = ['sender', 'recipient', 'content']
