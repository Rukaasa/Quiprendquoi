from django.forms import ModelForm

from recipes.models.contact import Students


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name' , 'email' , 'section']