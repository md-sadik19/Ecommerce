from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('contacts/detail/<int:id>', detail, name="detail"),
    path('about/', about, name="about"),
    path('add-contact/', add_contact, name="add_contact"),
    path('delete-contact/<int:id>/', delete_contact, name="delete_contact"),
    path('edit-contact/<int:id>/', edit_contact, name="edit_contact")
]