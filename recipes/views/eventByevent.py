from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from recipes.models.event import Event
from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel
from recipes.models.item import Item


class EventsView(LoginRequiredMixin, ListView):
    template_name = 'event.html'
    model = Event

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(groupModel, pk=kwargs.get('group_id'))
        group_membership = GroupMembership.objects.filter(user=self.request.user.id, group=kwargs.get('group_id'))

        if not group.owner_id == request.user:
            if not group_membership:
                raise PermissionDenied

        group_id = kwargs.get('group_id')
        event_id = kwargs.get('event_id')
        context = {
            'group': groupModel.objects.filter(id=group_id).first(),
            'event': Event.objects.filter(id=event_id).first(),
            'object_list': self.model.objects.filter(group_id=kwargs.get('group_id')),
            'items': Item.objects.filter(event=event_id),
            'group_id': group_id,
            'event_id': event_id,
        }
        return render(request, self.template_name, context)






