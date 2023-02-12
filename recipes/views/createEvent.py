from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.shortcuts import render, get_object_or_404

from recipes.forms.createEvent import EventForm
from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel


class CreateEventView(LoginRequiredMixin, FormView):
    template_name = 'createEvents.html'
    form_class = EventForm
    success_url = reverse_lazy('index')
    login_url = "/../login"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['group_id'] = self.kwargs['group_id']
        return kwargs

    def form_valid(self, form):
        group = get_object_or_404(groupModel, pk=self.kwargs['group_id'])
        groupMemberships = GroupMembership.objects.filter(group=self.kwargs.get('group_id'), user=self.request.user.id)

        if not group.owner_id == self.request.user:
            if not groupMemberships.user == self.request.user:
                return render(self.request, self.template_name, {'error': "Vous n'êtes pas le créateur de ce groupe."})
        form.save()
        return super().form_valid(form)

