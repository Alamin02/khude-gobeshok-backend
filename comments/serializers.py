from rest_framework import serializers
from comments.models import Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.CharField(max_length=150)
    avatar = serializers.ImageField(source='commenter.profile.avatar.thumbnail', read_only=True)

    class Meta:
        model = Comment
        fields = ['project', 'commenter', 'description', 'time', 'parent', 'avatar']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['commenter'] = User.objects.get(username=ret['commenter']).username
        return ret

    def create(self, validated_data):
        data = validated_data.copy()

        # TODO: Add exception e.g: get_object_or_404
        data['commenter'] = User.objects.get(username=data['commenter'])
        return super(CommentSerializer, self).create(data)
