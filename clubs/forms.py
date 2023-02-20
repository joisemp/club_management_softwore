from django import forms
from . models import ClubProfile


class ClubCreateForm(forms.ModelForm):
    class Meta:
        model = ClubProfile
        fields = [
            'name',
            'description',
        ]


class ClubEditForm(forms.ModelForm):
    class Meta:
        model = ClubProfile
        fields = [
            'name',
            'description',
        ]
