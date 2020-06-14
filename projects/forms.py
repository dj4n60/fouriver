from django.forms import forms, ModelForm, CharField, ImageField, Widget
from django import forms
from projects.models import developerinfo, customerinfo


class EditDeveloperForm(ModelForm):
    class Meta:
        model = developerinfo
        fields = ['location', 'language', 'github', 'cv', 'profile_pic']


class EditCustomerForm(ModelForm):
    class Meta:
        model = customerinfo
        fields = ['location', 'disc', 'linkedin', 'profile_pic']
