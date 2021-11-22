import factory

from faker import Faker

from main.models import AddressBook

fake = Faker()


class AddressBookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AddressBook

    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = '380668008080'
    url = 'https://www.google.com'
    country = 'UA'
    city = 'City'
    street = 'Street'
    image = f'contact_pics/{first_name}_{last_name}/filename'
