from django.contrib import admin

from .models import AddressBook


@admin.register(AddressBook)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", 'url')
    list_filter = ("last_name", 'first_name')
