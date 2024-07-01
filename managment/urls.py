from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contacts/', contacts, name="contacts"),
    path('contacts/detail/<int:id>', detail, name="detail"),
    path('about/', about, name="about"),
]