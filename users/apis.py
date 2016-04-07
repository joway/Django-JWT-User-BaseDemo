from django.http import response
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route

from rest_framework import permissions
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet, ):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]

    @list_route()
    def recent_users(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

