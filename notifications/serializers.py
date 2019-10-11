from rest_framework import serializers
from notifications.models import Notification
from users.models import User
from projects.models import Project
from comments.models import Comment


class NotificationRelatedField(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        if isinstance(value, User):
            return value.username
        if isinstance(value, Project):
            return value.title
        if isinstance(value, Comment):
            return value.description
        else:
            raise Exception("Unexpected Object Type")


class NotificationSerializer(serializers.ModelSerializer):
    actor = NotificationRelatedField(read_only=True)
    target = NotificationRelatedField(read_only=True)
    action_object = NotificationRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = [
            'level',
            'recipient',
            'unread',
            'actor',
            'verb',
            'description',
            'target',
            'action_object',
            'timestamp',
        ]
