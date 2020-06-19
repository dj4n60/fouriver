from django.forms import forms, ModelForm, CharField, ImageField, Widget
from django import forms
from projects.models import developerinfo, customerinfo


class EditDeveloperForm(ModelForm):
    location = forms.CharField(max_length=50, required=False),
    language = forms.CharField(max_length=50, required=False),
    github = forms.CharField(max_length=100, required=False),
    cv = forms.CharField(max_length=100, required=False),
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = developerinfo
        fields = ['location', 'language', 'github', 'cv', 'profile_pic']


class EditCustomerForm(ModelForm):
    location = forms.CharField(max_length=50, required=False),
    language = forms.CharField(max_length=50, required=False),
    linkedin = forms.CharField(max_length=100, required=False),
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = customerinfo
        fields = ['location', 'disc', 'linkedin', 'profile_pic']
