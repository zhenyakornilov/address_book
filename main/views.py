from django.db import transaction
from django.shortcuts import redirect
from django.views.generic import CreateView

from .forms import AddressBookForm
from .models import AddressBook


class AddressBookCreateView(CreateView):
    template_name = 'main/address_book_form.html'
    form_class = AddressBookForm
    success_url = ''

    @transaction.atomic
    def form_valid(self, form):
        AddressBook.objects.create(**form.cleaned_data)
        return redirect('/')
