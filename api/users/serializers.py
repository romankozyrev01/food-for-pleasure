from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    last_login = serializers.ReadOnlyField()
    is_superuser = serializers.ReadOnlyField()
    is_staff = serializers.ReadOnlyField()
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = CustomUser
        exclude = ['password', 'is_active', 'groups', 'user_permissions']
