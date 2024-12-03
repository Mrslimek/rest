from django import forms
from .models import Sun


class SunForm(forms.ModelForm):
    
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'placeholder': 'Name'
    }))

    class Meta:
        model = Sun
        fields = '__all__'

