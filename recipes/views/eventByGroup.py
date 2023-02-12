from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from recipes.models.event import Event
from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel


class GroupEventsListView(LoginRequiredMixin, ListView):
    template_name = 'eventListGroup.html'
    model = Event

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(groupModel, pk=kwargs.get('group_id'))
        groupMemberships = GroupMembership.objects.filter(group=kwargs.get('group_id'), user=self.request.user.id)
        if not group.owner_id == request.user:
            if not groupMemberships:
                raise PermissionDenied
        context = {
            'group_id': kwargs.get('group_id'),
            'object_list': self.model.objects.filter(group_id=kwargs.get('group_id')),
            'theGroup': groupModel.objects.filter(id=kwargs.get('group_id')).first(),
        }
        return render(request, self.template_name, context)











