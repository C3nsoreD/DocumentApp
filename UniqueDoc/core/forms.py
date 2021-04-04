from django import forms

from .models import Document

class DocumentForm(forms.Form):

    class Meta:
        model = Document

        fields = ('description', 'file',)
