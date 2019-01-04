from django import forms
from comments.models import Comment


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'post')
        widgets = {'post': forms.HiddenInput()}
