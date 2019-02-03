from django import forms

from photos.models import Photo


class PhotoAddForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('img', 'description','tags')
