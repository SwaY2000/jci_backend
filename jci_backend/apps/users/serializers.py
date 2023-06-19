from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model

from .models import UserModel as User

UserModel: User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'name', 'surname', 'is_superuser', 'last_login')

        read_only_fields = ('id', 'is_superuser', 'last_login')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
