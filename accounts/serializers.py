from rest_framework import serializers
from accounts.models import User, Family

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.role == 'PARENT':
            Family.objects.create(parent=user, family_name=f"{user.username}'s Family")
        return user
