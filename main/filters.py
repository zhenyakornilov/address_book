import django_filters

from .models import AddressBook


class AddressBookFilter(django_filters.FilterSet):
    class Meta:
        model = AddressBook
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'city': ['icontains'],
            'country': ['exact'],
            'street': ['icontains'],
            'url': ['icontains'],
            'phone_number': ['icontains'],
        }
