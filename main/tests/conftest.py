import pytest

from .factories import AddressBookFactory


@pytest.fixture
@pytest.mark.django_db
def create_contact_in_address_book():
    contact = AddressBookFactory.create()
    return contact


