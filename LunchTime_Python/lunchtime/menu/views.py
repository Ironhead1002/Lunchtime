from rest_framework import status
from rest_framework.decorators import api_view
from .models import Menu
from rest_framework.response import Response
from .serializer import MenuSerializer
import datetime


@api_view(["POST"])
def createMenu(request):
    a = request.data.get("menu")
    z = a
    menu_obj = Menu.objects.create(menu=z, latest_date=datetime.datetime.now())
    serializer = MenuSerializer(menu_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(["GET"])
def getMenu(request):
    try:
        data = Menu.objects.order_by('-latest_date').first()
        print(data.food_id)
        if data:
            listed_menu = eval(data.menu)
            menu_dict = {}
            counter = 0
            for i in listed_menu:
                menu_dict[counter] = i
                counter += 1
            return Response(menu_dict)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        print(e)
