# Create your views here.
from rest_framework import status
from .serializer import ReviewsSerializer
from rest_framework.decorators import api_view
from menu.models import Menu
from .models import Reviews
from rest_framework.response import Response


@api_view(['GET'])
def GetReview(request):
    latest_menu = Menu.objects.order_by('-latest_date').first()
    reviews = Reviews.objects.filter(menu_id=latest_menu)
    serializer = ReviewsSerializer(reviews, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@ api_view(['POST'])
def AddReview(request):
    latest_menu = Menu.objects.order_by('-latest_date').first()
    review = Reviews.objects.create(menu_id=latest_menu,
                                    menu_rev_star=request.data.get('star'),
                                    menu_rev_comment=request.data.get('comment'))
    serializer = ReviewsSerializer(review, data=request.data)
    if serializer.is_valid():
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
