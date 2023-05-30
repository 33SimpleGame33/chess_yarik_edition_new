from django import forms
from .models import Player,Competition
from django.core.exceptions import ValidationError

   
def even_selection_validator(value):
    if len(value) % 2 != 0:
        raise ValidationError('Please select an even number of items.')


class PlayerForm(forms.ModelForm):
    name = forms.CharField(max_length=10, min_length=2, required=True)

    class Meta:
        model = Player
        fields = ['name']

class CompetitionForm(forms.ModelForm):
    
    class Meta:
        model = Competition
        fields = ['players']

