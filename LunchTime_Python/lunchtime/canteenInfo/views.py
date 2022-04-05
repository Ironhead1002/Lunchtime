from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from userdetail.models import Profile
from .models import CanteenInfo
from django.contrib.auth.models import User
from .serializers import CanteenInfoSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


@api_view(["PUT", "GET"])
def UpdateCounter(request, pk):
    pro = Profile.objects.get(profile_id=pk)
    course = CanteenInfo.objects.filter(profile_id=pro).first()
    print(course)
    course.active_or_not = True
    print("Active True")
    serializer = CanteenInfoSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors)


@api_view(["PUT", "GET"])
def UpdateCounterDeactivate(request, pk):
    pro = Profile.objects.get(profile_id=pk)
    course = CanteenInfo.objects.filter(profile_id=pro).first()
    print(course)
    course.active_or_not = False
    print("Active True")
    serializer = CanteenInfoSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors)


@api_view(["GET"])
def GetCounter(request):
    pro = CanteenInfo.objects.filter(active_or_not=True).count()
    print(pro)
    return Response({"pro": pro})

# @api_view(["GET"])
# def UpdateCounter(request, pk):
#     pro = Profile.objects.get(profile_id=pk)
#     course = CanteenInfo.objects.filter(profile_id=pro).first()
#     print(course)
#     course.active_or_not = True
#     print("Active True")
#     serializer = CanteenInfoSerializer(course, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#     return Response(serializer.errors)
