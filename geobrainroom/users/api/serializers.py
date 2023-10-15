from rest_framework import serializers
from users.models import Users


class UserSerialiser(serializers.ModelSerializer):
    """
    serialize user data
    """
    class Meta:
        model = Users
        fields = '__all__'

