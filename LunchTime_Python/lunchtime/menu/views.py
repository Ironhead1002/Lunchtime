from django.shortcuts import render
from rest_framework import status
import json
from .serializer import MenuSerializer
from rest_framework.decorators import api_view
# Create your views here.
from .models import Menu
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import MenuSerializer
from rest_framework.viewsets import ModelViewSet
import json
from types import SimpleNamespace


# class MenuView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = MenuSerializer
@api_view(["POST"])
def createMenu(request):
    # import pdb
    # pdb.set_trace()
    a = request.data.get("menu")
    z = a

    # print(type(b))
    # print(b)
    menu_obj = Menu.objects.create(menu=z, latest_date=request.data.get("time"))
    # print(menu_obj)
    serializer = MenuSerializer(menu_obj, data=request.data)
    # print(serializer)
    if serializer.is_valid():
        # print("IN")
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["GET"])
def getMenu(request, pk):
    try:
        data = Menu.objects.filter(latest_date=pk).first()
        if data:
            a = eval(data.menu)
            b = {}
            c = 0
            for i in a:
                b[c] = i
                c += 1
            serializer = MenuSerializer(data)
            return Response(b)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        print(e)
