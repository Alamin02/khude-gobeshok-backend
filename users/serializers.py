from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User, Profile, Education, Job
from contents.serializers import ProfileImageSerializer


class UserSerializer(ModelSerializer):
    avatar = ProfileImageSerializer(source='profile.avatar')

    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined', 'avatar']


class ProfileSerializer(ModelSerializer):
    avatar = ProfileImageSerializer(required=False)

    class Meta:
        model = Profile
        fields = [
            'full_name',
            'bio',
            'avatar',
            'specialized_in',
            'software_skills',
            'phone_number',
            'country',
            'address',
        ]


class SquadSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'date_joined', 'profile']


class ProfileBioSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio']


class ProfileSpecializedInSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['specialized_in']


class ProfileSoftwareSkillSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['software_skills']


class EducationListSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'user', 'institute', 'major', 'degree', 'start_date', 'end_date', 'currently_enrolled']


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'institute', 'major', 'degree', 'start_date', 'end_date', 'currently_enrolled']


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'company', 'position', 'start_date', 'end_date', 'currently_working']


class UpdateProfilePicSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar']
