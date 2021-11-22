from main.models import AddressBook

import pytest

from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db(reset_sequences=True)
def test_address_book_record_creation(create_contact_in_address_book):
    assert AddressBook.objects.count() == 1


@pytest.mark.django_db(reset_sequences=True)
class TestAddressBookViews:
    def test_create_address_book_record_view(self, client, create_contact_in_address_book):
        response = client.get('/contacts/new/')
        assert response.status_code == 200
        assertTemplateUsed(response, 'main/address_book_form.html')

        response = client.post('/contacts/new/', data={'first_name': 'Name', 'last_name': 'Surname',
                                                       'phone_number': '380000000000', 'url': 'https://www.google.com'},
                               follow=True)
        assert response.status_code == 200
        assert AddressBook.objects.count() == 2
        assert AddressBook.objects.get(pk=2).first_name == 'Name'
        assert AddressBook.objects.get(pk=2).last_name == 'Surname'
        contact = AddressBook.objects.get(pk=2)
        redirect_url = response.redirect_chain[0][0]
        redirect_status_code = response.redirect_chain[0][1]
        assert redirect_url == f'/contacts/{contact.pk}/'
        assert redirect_status_code == 302


@pytest.mark.django_db(reset_sequences=True)
def test_handler_capitalize_contact_add_data(client, create_contact_in_address_book):
    assert AddressBook.objects.count() == 1
    contact = AddressBook.objects.get(pk=1)
    client.post(f'/contacts/{contact.pk}/edit/',
                data={'first_name': 'test', 'last_name': 'test2', 'city': 'toronto'})
    assert AddressBook.objects.get(pk=1).first_name == 'Test'
    assert AddressBook.objects.get(pk=1).last_name == 'Test2'
    assert AddressBook.objects.get(pk=1).city == 'Toronto'
