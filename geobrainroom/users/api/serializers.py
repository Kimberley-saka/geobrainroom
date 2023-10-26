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
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    

    def create(self, validated_data):
        """
        Create user with hashed password
        """
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

