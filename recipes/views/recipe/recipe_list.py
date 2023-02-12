from django.views.generic import ListView

from recipes.models.groupModel import groupModel


class RecipeListView(ListView):
    template_name = 'index.html'
    model = groupModel
