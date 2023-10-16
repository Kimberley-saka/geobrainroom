"""
data serializer
"""
from rest_framework import serializers
from users.models import Users


class UserSerialiser(serializers.ModelSerializer):
    """
    serialize user data
    """
    class Meta:
        """
        __summary__
        """
        model = Users
        fields = 'username', 'email', 'password'
