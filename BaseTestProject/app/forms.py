"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Persona
from django.contrib.admin.widgets import AdminDateWidget


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        exclude=['added', 'updated', 'is_enabled']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})
        }