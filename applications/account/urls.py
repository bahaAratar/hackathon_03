from django.urls import path, include
from applications.account.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django_rest_passwordreset.views import reset_password_request_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('myusers', MyUserdViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPIView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

# forgot password - email -> user.activation_code -> email
# forgiot password confirc -> p1, p2, email, activation_code -> user.password = 