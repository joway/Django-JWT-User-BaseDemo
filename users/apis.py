from django.http import response
from requests import Response
from rest_framework import viewsets
from rest_framework.decorators import list_route
from django.http import JsonResponse

from rest_framework import permissions
from .serializers import UserSerializer, UserRegistrationSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet, ):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny, ]

    @list_route(methods=['post'])
    def register(self, request):
        serialized = UserRegistrationSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                serialized.data['email'],
                serialized.data['password']
            )
            return JsonResponse({"status": "200", "message": "OK"})
        else:
            return JsonResponse({"status": "400", "message": serialized.errors})
