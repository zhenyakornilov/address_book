from django import forms

from django_countries.widgets import CountrySelectWidget

from .models import AddressBook


class AddressBookForm(forms.ModelForm):
    class Meta:
        model = AddressBook
        fields = ('first_name', 'last_name', 'country', 'city', 'street')
        widgets = {'country': CountrySelectWidget(),
                   'city': forms.TextInput(attrs={'placeholder': 'Optional'}),
                   'street': forms.TextInput(attrs={'placeholder': 'Optional'}),
                   }
