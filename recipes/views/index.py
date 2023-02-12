from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "homeDisconnect.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('panel')
        return super(IndexView, self).dispatch(request, *args, **kwargs)



