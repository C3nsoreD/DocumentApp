from django import forms

from .models import Document


class DocumentForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    class Meta:
        model = Document
        fields = ('title', 'description', 'classification' 'file',)
