from django import forms
from core.models import Gallery, Photo

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            'title',
            
        ]

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title',
            'description',
        ]


