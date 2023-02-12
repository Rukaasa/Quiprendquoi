from django import forms
from crispy_forms.helper import FormHelper
import crispy_forms.layout
from recipes.models.groupModel import groupModel


class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(crispy_forms.layout.Submit('submit', 'Create Group'))


    class Meta:
        model = groupModel
        fields = ['name', 'description']