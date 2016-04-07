from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'username', 'school', 'sex', 'birthday',
                  'score', 'is_staff', 'is_active', 'date_joined', 'subscribed',
                  'is_activated')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
