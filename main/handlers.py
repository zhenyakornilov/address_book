from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import AddressBook


@receiver(pre_save, sender=AddressBook)
def capitalize_add_contact_data(sender, **kwargs):
    if first_name := kwargs['instance'].first_name:
        kwargs['instance'].first_name = first_name.capitalize()
    if last_name := kwargs['instance'].last_name:
        kwargs['instance'].last_name = last_name.capitalize()
    if city := kwargs['instance'].city:
        kwargs['instance'].city = city.capitalize()
