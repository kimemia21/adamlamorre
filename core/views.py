from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from .serializer import UserSerializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
def all(request):
    querySet =User.objects.all()
    serializer =UserSerializer(querySet,many=True)
    
    # if serializer.is_valid():
        
    return Response(serializer.data,status=status.HTTP_200_OK)
    # else:
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def login(request):
    data =request.data
    print("block one")
    user =get_object_or_404(User,username =data["username"])
    print(f"block two {user}")
    if not user.check_password(data["password"]):
        print("block3")
        return Response({"Details":"User Not Found"},status=status.HTTP_400_BAD_REQUEST) 
    token,created  =Token.objects.get_or_create(user=user)
    serialzer =UserSerializer(user)
    print("block4")
    return Response({"user":serialzer.data,"token":token.key})
    
    
    
    return Response({"message":"success"})


@api_view(["POST"])
def signup(request):
    serializer =UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user =User.objects.get(username=request.data["username"])
        
        user.set_password(request.data["password"])
        user.save()
        # print(user.password)
        token =Token.objects.create(user=user)
        return Response({"token":token.key ,"user":serializer.data},status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET"])
def test_token(request):
    return Response({"message":"success"})
