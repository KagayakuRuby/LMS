from django.urls import path,include
from .views import *

urlpatterns = [
    # path('profiles/',profile_list_view , name='profile-list'),
    path('profiles/', ProfileListVeiw.as_view() , name='profile-list'),
    path('profiles/<int:pk>/',profile_detail_view , name='profiles-detail')
]
