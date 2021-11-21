from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddressBookCreateView.as_view(), name='address-book'),
    path('contacts/', views.AddressBookListRecords.as_view(), name='list-records'),
    path('contacts/<int:pk>/', views.AddressBookRecordDetailView.as_view(), name='watch-contact'),
    path('contacts/edit/<int:pk>/', views.EditContactView.as_view(), name='edit-contact'),
    path('contacts/<int:pk>/remove/', views.DeleteContactView.as_view(), name='delete-contact')
]
