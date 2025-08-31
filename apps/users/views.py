from django.contrib.auth import get_user_model from rest_framework import generics, permissions from rest_framework.response import Response from rest_framework.decorators import api_view, permission_classes from .serializers import RegisterSerializer, UserSerializer_

User = get_user_model()

class RegisterView(generics.CreateAPIView): serializer_class = RegisterSerializer permission_classes = [permissions.AllowAny]

@api_view(['GET', 'PUT']) @permission_classes([permissions.IsAuthenticated]) def me(request): if request.method == 'GET': return Response(UserSerializer(request.user).data) serializer = UserSerializer(instance=request.user, data=request.data, partial=True) serializer.is_valid(raise_exception=True) serializer.save() return Response(serializer.data)
