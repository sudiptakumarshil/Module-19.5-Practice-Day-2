from django import forms
from .models import Album
from django.forms.widgets import NumberInput
import datetime


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

        widgets = {
            'musician': forms.Select(attrs={'class': 'select2'}),
            'release_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'datepicker'}
            ),
            'rating': forms.Select(
                choices=[(i, i) for i in range(1, 6)], attrs={'class': 'select2'}
            )
        }

    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['release_date'].initial = datetime.date.today
