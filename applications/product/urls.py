from django.urls import path
from .views import ProductList, ProductCreate, ProductUpdate, ProductDelite

urlpatterns = [
    path('prosuct/',ProductList.as_view()),
    path('prosuct/<int:pk>/',ProductCreate.as_view()),
    path('prosuct/<int:pk>/',ProductUpdate.as_view()),
    path('product/<int:pk>/', ProductDelite.as_view())
]
