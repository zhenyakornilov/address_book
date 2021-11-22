from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .filters import AddressBookFilter
from .forms import AddressBookForm
from .models import AddressBook


class AddressBookCreateView(SuccessMessageMixin, CreateView):
    template_name = 'main/address_book_form.html'
    form_class = AddressBookForm
    success_message = 'Record saved successfully!'

    @transaction.atomic
    def get_success_url(self):
        return reverse('watch-contact', kwargs={'pk': self.object.pk})


class AddressBookListRecords(ListView):
    model = AddressBook
    template_name = 'main/address_book_list.html'
    paginate_by = 10
    filterset_class = AddressBookFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
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

    def get_success_url(self):
        return reverse('watch-contact', kwargs={'pk': self.object.pk})


class DeleteContactView(DeleteView):
    model = AddressBook
    success_url = reverse_lazy('list-records')
    template_name = 'main/address_book_confirm_delete.html'
    context_object_name = 'address_book'

    def get_object(self, **kwargs):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(AddressBook, pk=pk_)
