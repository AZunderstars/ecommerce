from django.contrib.auth import password_validation
from django.core.validators import RegexValidator
from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate_password(self, value):
        password_validation.validate_password(password=value)
        return value

    def validate_phone_number(self, value):
        validator = RegexValidator(regex=r'^09[0-9]{9}$')
        validator(value)
        return value
