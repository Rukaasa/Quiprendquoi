from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from recipes.forms.createGroup import GroupForm


class CreateGroupView(LoginRequiredMixin, FormView):
    template_name = 'createGroups.html'
    form_class = GroupForm
    success_url = reverse_lazy('index')
    login_url = "../login"

    def form_valid(self, form):
        form.instance.owner_id = self.request.user
        form.save()
        return super().form_valid(form)
