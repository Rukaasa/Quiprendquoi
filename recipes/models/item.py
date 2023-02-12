from django.contrib.auth.models import User
from django.db import models

from recipes.models.event import Event
from recipes.models.groupModel import groupModel


class Item(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(groupModel, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

