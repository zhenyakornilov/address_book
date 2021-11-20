from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddressBookCreateView.as_view(), name='address-book')
]
