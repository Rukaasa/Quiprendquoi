from django.shortcuts import render
from django.views.generic import ListView

from recipes.models.event import Event


class eventView(ListView):
    template_name = 'event.html'
    model = Event

