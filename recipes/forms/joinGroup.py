from django import forms
from recipes.models.groupModel import groupModel


class JoinGroupForm(forms.Form):
    key_invitation = forms.CharField(max_length=255, label='Rentrez une clé d\'invitation')

    def clean_key_invitation(self):
        key_invitation = self.cleaned_data.get('key_invitation')
        try:
            group = groupModel.objects.get(key_invitation=key_invitation)
        except groupModel.DoesNotExist:
            raise forms.ValidationError("Clé d'invitation incorrecte")
        return key_invitation
