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
        # super().save(last_login=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserListView(generics.GenericAPIView):
    serializer_class = UserListserializer
    pagination_class = (IsAuthenticated,)

    def get(self,request):
        user = request.user
        if user.role != 'admin':
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status.HTTP_403_FORBIDDEN)
        else:
            users = User.objects.filter(role='user').order_by('-id')
            serializer = self.serializer_class(users, many=True)
            count=0
            for i in users:
                 count +=1
            response = {
                'total user': count,
                'success': True,
                'status_code': status.HTTP_200_OK,
                'message': 'Successfully fetched users',
                'users': serializer.data

            }
            return Response(response, status=status.HTTP_200_OK)