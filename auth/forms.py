from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(label='user', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
