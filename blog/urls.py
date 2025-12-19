from django.urls import path,include
from .views import *

from .views import *
urlpatterns = [
    path('home/',my_view,name='home'),
    path('article/<int:article_id>/', article_id , name='article_id')
]