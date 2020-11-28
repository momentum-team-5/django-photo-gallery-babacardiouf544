from django import forms
from core.models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            'title',
            'is_private'
        ]