from django.urls import path, include
from .views import ReviewView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('register',RegisterView,basename='register')

router.register('feedback',ReviewView,basename='feedback')
urlpatterns = [
    path('', include(router.urls)),
]
