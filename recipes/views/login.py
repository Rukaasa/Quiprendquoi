from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.views.generic import FormView
from django.contrib import messages

from recipes.forms.login import UserLoginForm


class UserLoginView(FormView):
    template_name = "login.html"
    form_class = UserLoginForm

    def form_valid(self, form):
        form = AuthenticationForm(request=self.request, data=self.request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )
            if user is not None:
                login(self.request, user)
            messages.info(self.request, f'Welcome back {user.username} !')

            return redirect('index')

        else:

            messages.error(self.request, f'We cannot find this account')
            return super().form_invalid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().get(*args, **kwargs)