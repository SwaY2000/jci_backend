import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from .jwt_service import JWTService, RecoveryToken


class EmailService:

    @staticmethod
    def __send_email(to: str, template_name: str, context: dict, subject=''):
        template = get_template(template_name)
        content = template.render(context)

        msg = EmailMultiAlternatives(subject, from_email=os.getenv('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(content, 'text/html')

        msg.send()

    @classmethod
    def recovery_password(cls, user):
        token = JWTService.create_token(user, RecoveryToken)
        url = f'http://localhost:3000/recovery/{token}'
        cls.__send_email(user.email, 'recovery_password_email.html', {'name': user.name, 'url': url},
                         'Recovery Password')
