from django import forms
from .models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'public',
            'photo',
            'owner',
        ]
        widgets = {
            'photo': forms.FileInput(attrs={'class': "pa2 f4 w-100"})
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'featured_photo',
            'public',
            'owner'
        ]