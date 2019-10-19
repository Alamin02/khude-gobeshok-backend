from rest_framework import serializers
from notifications.models import Notification
from users.models import User
from projects.models import Project
from comments.models import Comment
from users.serializers import UserSerializer
from projects.serializers import ProjectListSerializer
from comments.serializers import CommentSerializer


class NotificationRelatedField(serializers.RelatedField):
    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        if isinstance(value, User):
            user = UserSerializer(value)
            return {'type': 'user', 'data': user.data}
        if isinstance(value, Project):
            project = ProjectListSerializer(value)
            return {'type': 'project', 'data': project.data}
        if isinstance(value, Comment):
            comment = CommentSerializer(value)
            return {'type': 'project', 'data': comment.data}
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
