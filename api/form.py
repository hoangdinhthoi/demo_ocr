from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
import ast
from django import forms
from api import field_validator


class OcrForm(forms.Form):
    image = forms.CharField(required=True)
    location = forms.CharField(required=True)
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
