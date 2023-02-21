from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    organisation_name = forms.CharField(widget=forms.TextInput(attrs={'required':True}))
    class Meta:
        model = User
        fields = ['organisation_name','email']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'required': True}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'required': True}))
    remember_me = forms.BooleanField(required=False)