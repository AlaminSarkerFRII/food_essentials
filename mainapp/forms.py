from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordResetForm
from django.contrib.auth.models import User





class LoginForm(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))
    

class CustormerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))

    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'autofocus': 'True', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email','password1']



class MyPasswordResetForm(PasswordResetForm):
        pass
    # username = UsernameField(widget=forms.TextInput(
    #     attrs={'autofocus': 'True', 'class': 'form-control'}))
    # password = forms.CharField(label='Password', widget=forms.PasswordInput(
    #     attrs={'autocomplete': 'current-password', 'class': 'form-control'}))