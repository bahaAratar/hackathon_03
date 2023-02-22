from django.urls import path, include
from applications.feedback.views import *
from rest_framework.routers import DefaultRouter
from applications.product.views import *

    
router = DefaultRouter()
# router.register('comments', CommentViewSet, basename='comment')
router.register('comment', CommentModelViewSet)
router.register('rating', RatingModelViewSet)
router.register('', FavoriteModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
