from rest_framework import serializers
from .models import DirectMessage
from users.models import User


class ConversationSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(max_length=150)
    recipient = serializers.CharField(max_length=150)
    avatar = serializers.ImageField(
        source='sender.profile.avatar.thumbnail',
        read_only=True,
    )

    class Meta:
        model = DirectMessage
        fields = [
            'sender',
            'recipient',
            'content',
            'sent_at',
            'sender_name',
            'recipient_name',
            'avatar',
        ]

    sender_name = serializers.SerializerMethodField('get_sender_name')
    recipient_name = serializers.SerializerMethodField('get_recipient_name')

    @staticmethod
    def get_sender_name(obj):
        return obj.sender.username

    @staticmethod
    def get_recipient_name(obj):
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
