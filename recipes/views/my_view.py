from django.shortcuts import render

from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel


def my_view(request):
    groups = groupModel.objects.all()
    memberships = GroupMembership.objects.all()
    context = {
        'groups': groups,
        'memberships': memberships,
    }
    return render(request, 'my_template.html', context)