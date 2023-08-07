from django.urls import path

from .views import ContactListView, ContactView


urlpatterns = [
    path('contactlist/', ContactListView.as_view(), name='contact_list'),
    path('contactlist/<int:contact_id>/', ContactView.as_view(), name='contact'),
]
