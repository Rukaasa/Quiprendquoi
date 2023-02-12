from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from recipes.models.event import Event


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        group_id = kwargs.pop('group_id')
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create Event'))
        self.fields['group_id'].initial = group_id

    class Meta:
        model = Event
        fields = ['name', 'event_date', 'description', 'group_id']
        widgets = {'group_id': forms.HiddenInput()}
