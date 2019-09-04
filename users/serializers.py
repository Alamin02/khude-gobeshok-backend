from rest_framework.serializers import ModelSerializer
from .models import User, Profile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'phone_number', 'country', 'address']
