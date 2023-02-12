from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from recipes.forms.createItem import ItemForm
from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel


class ItemCreateView(LoginRequiredMixin, FormView):
    template_name = 'createItem.html'
    form_class = ItemForm
    success_url = reverse_lazy('index')
    login_url = "../login"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['group_id'] = self.kwargs['group_id']
        kwargs['event_id'] = self.kwargs['event_id']
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def form_valid(self, form, **kwargs):
        group_membership = GroupMembership.objects.filter(user=self.request.user.id, group_id=self.kwargs['group_id']).first()
        group_owner = groupModel.objects.filter(owner_id=self.request.user.id, id=self.kwargs['group_id']).first()
        if group_owner is None:
            if group_membership is None:
                return render(self.request, 'createItem.html', {'error': 'Tu ne fais pas partie du groupe.'})
        form.save()
        return super().form_valid(form)
