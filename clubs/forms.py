from django import forms
from . models import ClubProfile

class ClubDetailForm(forms.ModelForm):
    class Meta:
        model = ClubProfile
        fields = [
            'name',
            'description',
        ]