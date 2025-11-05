from django.urls import path,include

urlpatterns = [
    path('signup/',signupView,name="sign-up")
]
