from django.contrib.auth import get_user_model from rest_framework import serializers_

User = get_user_model()

class UserSerializer(serializers.ModelSerializer): class Meta: model = User fields = ['id', 'email', 'first_name', 'last_name', 'role']

class RegisterSerializer(serializers.ModelSerializer): password = serializers.CharField(write_only=True, min_length=8)

class Meta: model = User fields = ['email', 'password', 'first_name', 'last_name']

def create(self, validated_data):
    email = validated_data['email']
    password = validated_data.pop('password')
    user = User(**validated_data)
    user.username = email
    user.set_password(password)
    user.save()
    return user**_
