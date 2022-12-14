from rest_framework.serializers import ModelSerializer

from .models import UserModel


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email']


class StaffUserSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff']
