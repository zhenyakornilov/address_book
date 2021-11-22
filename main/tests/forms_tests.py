from main.forms import AddressBookForm

import pytest


@pytest.mark.django_db
class TestAddressBookForm:
    def test_url_valid(self):
        form = AddressBookForm(data={'first_name': 'test', 'last_name': 'test', 'url': 'https://www.google.com/'})
        assert form.is_valid()

    def test_url_invalid(self):
        form = AddressBookForm(data={'first_name': 'test', 'last_name': 'test', 'url': 'bad_url'})
        assert not form.is_valid()

    def test_phone_invalid(self):
        form = AddressBookForm(data={'first_name': 'test', 'last_name': 'test', 'phone_number': 'bad_number'})
        assert not form.is_valid()

    def test_phone_valid(self):
        form = AddressBookForm(data={'first_name': 'test', 'last_name': 'test',
                                     'phone_number': '0660000000', 'country': 'UA'})
        assert form.is_valid()

    def test_empty_form(self):
        form = AddressBookForm(data={})
        assert not form.is_valid()
