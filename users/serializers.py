from rest_framework.serializers import ModelSerializer
from .models import User, Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileCreateSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_owner']
