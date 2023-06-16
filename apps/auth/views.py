from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response

from .serializers import TokenPairSerializer, EmailSerializer, PasswordSerializer
from core.services.email_service import EmailService
from core.services.jwt_service import JWTService, RecoveryToken

from ..users.models import UserModel as User

UserModel: User = get_user_model()

class TokenPairView(TokenObtainPairView):
    """
    Login
    """
    serializer_class = TokenPairSerializer


class CheckUserAndGetEmailForRecovery(GenericAPIView):
    def get_serializer(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        data = self.request.data

        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user_in_db = get_object_or_404(UserModel, email=serializer.data["email"])

        EmailService.recovery_password(user_in_db)

        return Response('Check your email', status=status.HTTP_200_OK)


class RecoveryPassword(GenericAPIView):
    def get_serializer(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        data = self.request.data

        token = kwargs["token"]

        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = JWTService.validate_token(token, RecoveryToken)

        user.set_password(serializer.data["password"])
        user.save()

        return Response(status=status.HTTP_200_OK)
