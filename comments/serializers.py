from rest_framework import serializers
from comments.models import Comment


class CommentSerialzer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['project', 'commenter', 'description', 'time', 'parent']
