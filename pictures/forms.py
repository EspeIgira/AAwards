from django import forms
from .models import Picture,Profile

class SignUpForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['user', 'pub_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'pub_date']
