from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from recipes.models.event import Event
from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel
from recipes.models.item import Item


class Panel(LoginRequiredMixin, ListView):
    template_name = 'homeConnect.html'
    model = groupModel
    login_url = '/login'

    def get(self, request, **kwargs):
        groups = groupModel.objects.filter(owner_id=self.request.user)
        Mymemberships = GroupMembership.objects.filter(group__in=groups)
        memberships = GroupMembership.objects.filter(user=self.request.user)
        groups_joins = groupModel.objects.filter(id__in=memberships.values_list('group', flat=True))
        events = Event.objects.filter(group_id__in=groups)
        item = Item.objects.filter(group__in=groups)
        context = {
            'groups': groups,
            'events': events,
            'groups_joins': groups_joins,
            'item': item,
            'Mymemberships': Mymemberships,
        }
        return render(request, 'homeConnect.html', context)




