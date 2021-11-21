from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .filters import AddressBookFilter
from .forms import AddressBookForm
from .models import AddressBook


class AddressBookCreateView(SuccessMessageMixin, CreateView):
    template_name = 'main/address_book_form.html'
    form_class = AddressBookForm
    success_message = 'Record saved successfully!'

    @transaction.atomic
    def form_valid(self, form):
        AddressBook.objects.create(**form.cleaned_data)
        return redirect('list-records')


class AddressBookListRecords(ListView):
    model = AddressBook
    template_name = 'main/address_book_list.html'
    queryset = AddressBook.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AddressBookFilter(self.request.GET, queryset=self.get_queryset())
        return context


class AddressBookRecordDetailView(DetailView):
    model = AddressBook
    template_name = 'main/address_book_detail.html'
    context_object_name = 'address_book'
    queryset = AddressBook.objects.all()

    def get_object(self, **kwargs):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AddressBook, pk=pk_)


class EditContactView(UpdateView):
    model = AddressBook
    template_name = 'main/address_book_edit.html'
    form_class = AddressBookForm
    success_url = reverse_lazy('list-records')


class DeleteContactView(DeleteView):
    model = AddressBook
    success_url = reverse_lazy('list-records')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
