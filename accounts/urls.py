from django.urls import path,include
from .views import *

urlpatterns = [
    path('signup/',UserRegisterView.as_view() ,name='signup'),
    path('login/', UserLoginView.as_view() , name='login'),
    path('logout/', user_logout_view, name='logout')

]