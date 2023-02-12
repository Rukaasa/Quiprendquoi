from django.views.generic import CreateView

from recipes.models.tag import Tag


class TagCreateView(CreateView):
    template_name = 'tag_create_view.html'
    model = Tag
    fields = ['text']

    def get_success_url(self):
        return reversed('tag_list')