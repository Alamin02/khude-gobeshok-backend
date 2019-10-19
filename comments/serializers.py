from rest_framework import serializers
from comments.models import Comment
from users.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.CharField(max_length=150, read_only=True)
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
        try:
            data['commenter'] = User.objects.get(username=self.context.get('user'))
        except ObjectDoesNotExist:
            return ValidationError('User does not exist, strange!')
        return super(CommentSerializer, self).create(data)
