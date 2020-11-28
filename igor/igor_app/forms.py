from django import forms
from django.forms import ModelForm
from .models import Profile



class ProfileForm(forms.Form):
    first_name=forms.CharField(max_length=20, required=True)
    occupation=forms.CharField(max_length=20, required=True)
    about=forms.CharField(widget=forms.Textarea, required=True)
    img=forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = '__all__'
