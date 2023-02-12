from django import forms

from recipes.models.event import Event
from recipes.models.groupModel import groupModel


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'description')

    group = forms.ModelChoiceField(queryset=groupModel.objects.all(), widget=forms.HiddenInput())
    event_date = forms.DateTimeField(widget=forms.SelectDateWidget())
    description = forms.CharField(widget=forms.Textarea(attrs={'maxlength': 300}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['group'].initial = self.request.user.id

# Ce formulaire utilise la classe ModelForm de Django pour créer un formulaire
# à partir du modèle Event. Il inclut les champs name, event_date et description,
# ainsi qu'un champ caché pour le group-id qui est automatiquement généré en fonction
# de l'utilisateur connecté. La date de l'événement est sélectionnée à l'aide d'un widget
# de calendrier, et la description est limitée à 300 caractères.
#
# Il faudra donc ajouter à votre vue le traitement pour récupérer l'id du groupe
# selectionné pour l'utiliser dans le formulaire.