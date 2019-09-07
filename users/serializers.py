from rest_framework.serializers import ModelSerializer
from .models import User, Profile, Education


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name', 'bio', 'phone_number', 'country', 'address']


class EducationListSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'user', 'institute', 'major', 'degree', 'start_date', 'end_date', 'currently_enrolled']


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institute', 'degree', 'start_date', 'end_date', 'currently_enrolled']
