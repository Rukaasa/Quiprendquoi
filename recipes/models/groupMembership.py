from django.contrib.auth.models import User
from django.db import models
from recipes.models.groupModel import groupModel


class GroupMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(groupModel, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'group']
