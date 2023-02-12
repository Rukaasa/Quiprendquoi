from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from recipes.models.item import Item


class ItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        group_id = kwargs.pop('group_id')
        user_id = kwargs.pop('user_id')
        event_id = kwargs.pop('event_id')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create Event'))
        self.fields['group'].initial = group_id
        self.fields['user'].initial = user_id
        self.fields['event'].initial = event_id

    class Meta:
        model = Item
        fields = ['name', 'user', 'group', 'event']
        widgets = {'group': forms.HiddenInput(),
                   'user': forms.HiddenInput(),
                   'event': forms.HiddenInput(),
                   }
