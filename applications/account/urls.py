from django.urls import path, include
from applications.account.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    # path('password_reset/<token>', ResetPasswordView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')), 
]