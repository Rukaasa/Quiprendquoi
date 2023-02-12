from django.shortcuts import render
from django.views import View

from recipes.models.event import Event
from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel


class GroupInfoView(View):
    def get(self, request):
        groups = groupModel.objects.all()
        memberships = GroupMembership.objects.all()
        group = groupModel.objects.get(id=6)
        events = Event.objects.all()
        context = {
            'groups': groups,
            'events': events,
            'memberships': memberships.filter(group=group),
        }
        return render(request, 'group_details.html', context)