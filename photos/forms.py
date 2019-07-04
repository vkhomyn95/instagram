from django import forms

from photos.models import Photo, Lead


class PhotoAddForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('img', 'description','tags')


class MakeLeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = ('name', 'domain', 'id', 'uuid', 'roll_id')
