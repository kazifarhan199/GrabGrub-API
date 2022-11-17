from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

@property
def token(self):
    return str(Token.objects.get_or_create(user=self)[0])

User.add_to_class('token', token)
