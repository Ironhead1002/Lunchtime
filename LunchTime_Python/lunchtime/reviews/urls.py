from django.urls import path
from .views import AddReview, GetReview

urlpatterns = [
    path('feedback/', AddReview, name='feedback'),
    path('getfeedback/', GetReview, name='getfeedback'),
]
