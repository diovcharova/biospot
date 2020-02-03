from django import forms


class UserLoginForm(forms.Form):
    """Form to log in"""
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
