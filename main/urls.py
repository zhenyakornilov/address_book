from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddressBookCreateView.as_view(), name='address-book'),
    path('contacts/', views.AddressBookListRecords.as_view(), name='list-records'),
    path('contacts/<int:pk>/', views.AddressBookRecordDetailView.as_view(), name='watch-contact'),
]
