from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .serializer import ReviewsSerializer
from rest_framework.viewsets import ModelViewSet



class ReviewView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ReviewsSerializer