from django import forms
from .models import Property, Image

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
