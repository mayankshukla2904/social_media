from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import SystemLog, UserRole, ModeratorAction

User = get_user_model()


class SystemLogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True, default=None)

    class Meta:
        model = SystemLog
        fields = [
            'id', 'timestamp', 'level', 'type', 'user', 'username',
            'action', 'details', 'ip_address', 'user_agent'
        ]
        read_only_fields = ['id', 'timestamp']


class UserRoleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    created_by_username = serializers.CharField(
        source='created_by.username', read_only=True, default=None
    )

    class Meta:
        model = UserRole
        fields = [
            'id', 'user', 'username', 'role_type', 'permissions',
            'created_at', 'updated_at', 'created_by', 'created_by_username'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ModeratorActionSerializer(serializers.ModelSerializer):
    moderator_username = serializers.CharField(source='moderator.username', read_only=True)
    target_username = serializers.CharField(source='target_user.username', read_only=True)

    class Meta:
        model = ModeratorAction
        fields = [
            'id', 'moderator', 'moderator_username', 'action_type',
            'target_user', 'target_username', 'reason', 'details', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class AdminUserSerializer(serializers.ModelSerializer):
    role = UserRoleSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'is_staff', 'is_superuser',
            'is_active', 'date_joined', 'last_login', 'role'
        ]
        read_only_fields = ['id', 'date_joined', 'last_login']
