from django.urls import path
from .views import *


urlpatterns = [
    path('', UserRegistrationView.as_view(), name='Register'),
    path('login/', UserLoginView.as_view(), name='Login'),
    path('userlist/', UserListView.as_view(), name='user List'),



]