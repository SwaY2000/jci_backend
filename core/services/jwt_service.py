from django.contrib.auth import get_user_model
from typing import Type

from rest_framework import status
from rest_framework_simplejwt.tokens import BlacklistMixin, Token
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from core.enums.action_token_enum import ActionEnum

from apps.users.models import UserModel as User
from core.exceptions.jwt_exception import JWTException

UserModel: User = get_user_model()

ActionTokenClassType = Type[BlacklistMixin | Token]


class ActionToken(BlacklistMixin, Token):
    pass


class RecoveryToken(ActionToken):
    token_type = ActionEnum.RECOVERY.token_type
    lifetime = ActionEnum.RECOVERY.exp_time


class JWTService:

    @staticmethod
    def create_token(user, token_class: ActionTokenClassType):
        return token_class.for_user(user)

    @staticmethod
    def validate_token(token, token_class: ActionTokenClassType):
        try:
            token_res = token_class(token)
            token_res.check_blacklist()
        except (Exception,):
            raise JWTException

        token_res.blacklist()
        user_id = token_res.payload.get('user_id')
        return get_object_or_404(UserModel, pk=user_id)
