from django.urls import path, include
from applications.feedback.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('comments', CommentViewSet, basename='comment')
router.register('comment', CommentModelViewSet)
router.register('rating', RatingModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
