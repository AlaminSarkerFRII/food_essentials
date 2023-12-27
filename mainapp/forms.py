from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustormerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))

    email = forms.CharField(widget=forms.EmailInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))