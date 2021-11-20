from django.db import models


from django_countries.fields import CountryField


class AddressBook(models.Model):
    first_name = models.CharField(max_length=100, unique=False, db_column='First name')
    last_name = models.CharField(max_length=100, unique=False, db_column='Last name')
    country = CountryField(blank=True)
    city = models.CharField(blank=True, max_length=100, unique=False, db_column='City')
    street = models.CharField(blank=True, max_length=100, unique=False, db_column='Street')
    phone_number = models.CharField(blank=True, max_length=20, db_column='Phone number')
    url = models.URLField(blank=True, db_column='URL')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique fullname')
        ]
        ordering = ('first_name', 'last_name', )

    def __str__(self):
        return f'First name: {self.first_name}, ' \
               f'Last name: {self.last_name},'
