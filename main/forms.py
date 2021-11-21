import re

from django import forms
from django.core.validators import URLValidator
from django.core.validators import ValidationError

from django_countries.widgets import CountrySelectWidget

from .models import AddressBook


def validate_phone_number(form_phone_number):
    if not re.match(r"^\d{8,15}$", form_phone_number):
        raise ValidationError(f'{form_phone_number}: Enter digits only in phone number')


class AddressBookForm(forms.ModelForm):
    url = forms.CharField(label='URL', required=False, validators=[URLValidator])
    phone_number = forms.CharField(label='Phone number', required=False, validators=[validate_phone_number])
    image = forms.ImageField(label='Image', required=False)

    class Meta:
        model = AddressBook
        fields = ('first_name', 'last_name', 'country', 'city', 'street', 'phone_number', 'url', 'image')
        widgets = {'country': CountrySelectWidget(),
                   'city': forms.TextInput(attrs={'placeholder': 'Optional'}),
                   'street': forms.TextInput(attrs={'placeholder': 'Optional'})}
