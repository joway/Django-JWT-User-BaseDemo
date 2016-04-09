from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (JSONWebTokenAuthentication,)


def index(request):
    return render(request, "home.html")
