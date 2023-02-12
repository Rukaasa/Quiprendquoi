from django.db import models

from recipes.models.groupModel import groupModel


class Event(models.Model):
    group_id = models.ForeignKey(groupModel, on_delete=models.CASCADE, related_name='events')
    name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    event_date = models.DateTimeField()
    description = models.TextField()



