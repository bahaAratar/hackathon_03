from django.urls import path
from .views import ContactCreate, ContactList, ContactUpdate,ContactDelite

urlpatterns = [
    path('contacts/',ContactList.as_view()),
    path('contacts/<int:pk>/', ContactCreate.as_view()),
    path('contacts/<int:pk>/', ContactUpdate.as_view()),
    path('contacts/<int:pk>/', ContactDelite.as_view())
]