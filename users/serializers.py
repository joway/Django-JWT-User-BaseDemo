from rest_framework import serializers

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, min_length=6, max_length=200)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'password',
        )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    @staticmethod
    def init_data(obj):
        return obj.value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'username', 'school', 'sex', 'birthday',
                  'score', 'is_staff', 'is_active', 'date_joined', 'subscribed',
                  'is_activated')

        # def create(self, validated_data):
        #     pass
        #
        # def update(self, instance, validated_data):
        #     pass
