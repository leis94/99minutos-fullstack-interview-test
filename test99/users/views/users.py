"""Users views."""

# Django REST Framework
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from django.contrib.auth.models import User

# Serializers
from test99.users.serializers import (
    UserModelSerializer,
    UserLoginSerializer,
    UserSignUpSerializer,
)


class UserViewSet(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                viewsets.GenericViewSet):
    """User view set.
    Handle sign up and login.
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


    @action(detail=False, methods=['post'])
    def login(self, request):
        """User login up."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User signup up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)