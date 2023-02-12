from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from recipes.models.groupMembership import GroupMembership
from recipes.models.groupModel import groupModel


class JoinGroupView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'join_group.html')

    def post(self, request):
        invitation_key = request.POST.get('key_invitation')
        group = groupModel.objects.filter(key_invitation=invitation_key).first()

        if not group:
            return render(request, 'join_group.html', {'error': 'Invalid invitation key'})

        if request.user.id == group.owner_id.id:
            return render(request, 'join_group.html', {'error': 'Vous êtes déja le créateur de ce groupe'})

        if GroupMembership.objects.filter(user=request.user, group=group).exists():
            return render(request, 'join_group.html', {'error': 'Vous êtes déjà membre de ce groupe'})

        GroupMembership.objects.create(user=request.user, group=group)
        group.save()

        # pour supprimer:
        #         membership = GroupMembership.objects.get(user=request.user, group=group)
        #         membership.delete()

        return redirect('index')
