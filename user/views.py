from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics,status
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserRegistrationView(generics.GenericAPIView):
    serializer_class = NewUserSerializer
    def post(self, request, format=None):
       try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user_data = serializer.data
            return Response(user_data, status=status.HTTP_201_CREATED)
       except:
           return Response('user already_exists')
    
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        userdata = request.data
        # user1 = MyUser.objects.get(name=user['name'])
        # print(user1)
        serializer = self.serializer_class(data=userdata)
        valid = serializer.is_valid(raise_exception=True)
       
        return Response(serializer.data, status=status.HTTP_200_OK)
