from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if email.endswith('@syr.edu'):
            return email
        raise forms.ValidationError('Must be a syr.edu email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
