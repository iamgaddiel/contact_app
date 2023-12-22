from django import forms
from django.contrib.auth.models import User
from .models import Contact




# class CreateContactForm(forms.Form):
#     first_name = forms.CharField(max_length=300)
#     last_name = forms.CharField(max_length=300)
#     nickname = forms.CharField(max_length=300)
#     age = forms.IntegerField(max_value=30)



class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user']
        # fields = '__all__'
        # fields = ['nickname', 'phone', 'notes']


class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['user']

