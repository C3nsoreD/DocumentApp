from django import forms

from .models import User

# Comments for test
class UserForm(forms.Form):
    first_name = forms.CharField(label='First Name')
    Last_name = forms.CharField(label='Last Name')
    email = forms.CharField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ('first_name', 'last_name', 'email', 'password',)
