from django.urls import path, include
from applications.account.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django_rest_passwordreset.views import reset_password_request_token

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/', MyUsertList.as_view()),
    path('account/<int:pk>/', MyUserDetail.as_view()),
    # path('password_reset/confirm/', ...),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]