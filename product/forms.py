from django import forms
from .models import Commit


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commit
        fields = ('product', 'name', 'email', 'description')

