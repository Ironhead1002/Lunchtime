from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Profile
from rest_framework.views import APIView
from canteenInfo.models import CanteenInfo

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, ProfilegetSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        reg_serializer = RegisterSerializer(data=data)
        if reg_serializer.is_valid():
            password = reg_serializer.validated_data.get('password')
            reg_serializer.validated_data['password'] = make_password(password)
            new_user = reg_serializer.save()
            if new_user:
                return Response({"Id": new_user.id}, status=status.HTTP_200_OK)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def loginUserPage(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    password = serializer.validated_data['password']
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            context = {'email': user.email, 'username': user.username, 'Id': user.id}
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except BaseException as e:
        return Response(e, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createProfile(request):
    user = User.objects.get(id=request.data.get("pk"))
    profile = Profile.objects.create(user=user, department=request.data.get("department"), trainee_or_employee=request.data.get('trainee_or_employee'))
    info = CanteenInfo.objects.create(profile_id=profile, active_or_not=False)
    info.save()
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def retrieveProfile(request, pk):
    try:
        profile = Profile.objects.get(profile_id=pk)
        serializer = ProfilegetSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response(e, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def updateProfile(request, pk):
    try:
        profile = Profile.objects.get(profile_id=pk)
        serializer = ProfileSerializer(profile, request.data)
        if serializer.is_valid():
            print('Serializer is valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    except BaseException as e:
        return Response(e, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        user = User.objects.get(email=email)
        print(user)
        if user is not None:
            return Response(status.HTTP_200_OK)
        else:
            print("error")
    return "test"

