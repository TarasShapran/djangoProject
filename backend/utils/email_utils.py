import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from backend.enums.email_template import TemplateEnum
from rest_framework.request import Request
from rest_framework.reverse import reverse

from rest_framework_simplejwt.tokens import Token


class EmailUtils:
    @staticmethod
    def _send_mail(to: str, template_name: str, context: dict, subject='') -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'), to=[to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

    @classmethod
    def register_email(cls, address: str, name: str, token: Token, request: Request) -> None:
        uri = request.build_absolute_uri(reverse('auth_activate', args=(token,)))
        cls._send_mail(address, TemplateEnum.REGISTER.value, {'name': name, 'url': uri}, 'Register')

    @classmethod
    def recovery_password_email(cls, address: str, token: Token, request: Request) -> None:
        uri = request.build_absolute_uri(reverse('auth_recovery_password'))
        cls._send_mail(address, TemplateEnum.RECOVERY_PASSWORD.value, {'token': token, 'url': uri}, 'Recovery password')
