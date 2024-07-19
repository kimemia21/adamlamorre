from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from .serializer import UserSerializer

@api_view(["POST"])
def login(request):
    serializer =UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user =User.objects.get(username=request.data["username"])
        token =Token.created(user=user)
    return Response({"token":token.key,"user":serializer.data},status=status.HTTP_200_OK)

@api_view(["POST"])
def signup(request):
    return Response({"message":"success"})

@api_view(["GET"])
def test_token(request):
    return Response({"message":"success"})
