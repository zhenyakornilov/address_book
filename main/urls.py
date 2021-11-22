from django.urls import path

from . import views

urlpatterns = [
    path('contacts/new/', views.AddressBookCreateView.as_view(), name='address-book'),
    path('', views.AddressBookListRecords.as_view(), name='list-records'),
    path('contacts/<int:pk>/', views.AddressBookRecordDetailView.as_view(), name='watch-contact'),
    path('contacts/<int:pk>/edit/', views.EditContactView.as_view(), name='edit-contact'),
    path('contacts/<int:pk>/delete/', views.DeleteContactView.as_view(), name='delete-contact'),
]
