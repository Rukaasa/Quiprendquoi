from django.contrib.auth.models import User

from django.db import models

import secrets


def generate_key():
    return secrets.token_hex(6)


class groupModel(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    key_invitation = models.CharField(max_length=64, unique=True, default=generate_key)
