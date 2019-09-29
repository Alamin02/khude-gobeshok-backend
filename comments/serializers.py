from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['project', 'commenter', 'description', 'time', 'parent']
