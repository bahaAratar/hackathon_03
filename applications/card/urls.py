from django.urls import path
from .views import CardDetail, CardList,CardCreate,CardUpdate

urlpatterns = [
    path('cards/',CardList.as_view()),
    path('del_upd/<int:pk>/', CardDetail.as_view()),
]