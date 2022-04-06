from rest_framework import status
from rest_framework.decorators import api_view
from .models import Menu
from rest_framework.response import Response
from .serializer import MenuSerializer
import datetime


@api_view(["POST"])
def createMenu(request):
    the_menu = request.data.get("menu")
    menu_obj = Menu.objects.create(menu=the_menu, latest_date=datetime.datetime.now())
    serializer = MenuSerializer(menu_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def getMenu(request):
    try:
        data = Menu.objects.order_by('-latest_date').first()
        if data:
            listed_menu = eval(data.menu)
            menu_dict = {}
            counter = 0
            for i in listed_menu:
                menu_dict[counter] = i
                counter += 1
            return Response(menu_dict, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        return Response(e, status=status.HTTP_400_BAD_REQUEST)
