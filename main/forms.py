from django import forms
from django.core.validators import URLValidator

from django_countries.widgets import CountrySelectWidget

from .models import AddressBook


class AddressBookForm(forms.ModelForm):
    url = forms.CharField(label='URL', required=False, validators=[URLValidator])

    class Meta:
        model = AddressBook
        fields = ('first_name', 'last_name', 'country', 'city', 'street', 'phone_number', 'url')
        widgets = {'country': CountrySelectWidget(),
                   'city': forms.TextInput(attrs={'placeholder': 'Optional'}),
                   'street': forms.TextInput(attrs={'placeholder': 'Optional'}),
                   }
