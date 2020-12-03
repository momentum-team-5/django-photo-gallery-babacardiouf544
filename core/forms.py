from django import forms
from core.models import Gallery, Photo, Comment

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
            'default',
            'title',
            'image',
            'description',
        
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text",
        ]
