from django.http import JsonResponse
from django.views import View

from recipes.models.groupModel import groupModel


class GroupListJsonView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        result = groupModel.objects.all()
        return JsonResponse([a.title for a in result], safe=False)
