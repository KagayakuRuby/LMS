from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LogoutView,LoginView
from django.views.generic.edit import CreateView


# Create your views here.

def user_register_view(request):
    if request.method == 'POST':
        form = UserRegistionFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,f'کاربر {user.first_name} با موفقیت وارد شد.')
            return redirect('home')
        else:
            messages.error(request,'کاربر ثبت نشد!')
    else:
        form = UserRegistionFrom()

    return render(request,'register.html',{'form':form})

class UserRegisterView(CreateView):
    form_class = UserRegistionFrom
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request , self.object)
        messages.success(self.request,f'کاربر {self.object.first_name} با موفقیت وارد شد.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request,'ثبت انجام نشد.')
        return super().form_invalid(form)


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForms(request,date=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,f'کاربر {user.first_name} با موفقیت وارد شد.')
            return redirect('home')
        else:
            messages.error(request,'کاربر وارد نشد!')

    else:
        form = UserLoginForms()

    return render(request,'login.html',{'form':form})



class UserLoginView(LoginView):
    """
    سفارشی‌سازی LoginView برای نمایش پیام موفقیت پس از ورود.
    """
    form_class   = UserLoginForms
    template_name = "login.html"
    success_url   = reverse_lazy("home")

    def form_valid(self, form):
        # LoginView خودش کاربر را لاگین می‌کند.
        response = super().form_valid(form)

        # کاربر لاگین شده در request.user موجود است.
        user = self.request.user   # یا user = form.get_user()
        messages.success(
            self.request,
            f"کاربر {user.first_name} با موفقیت وارد شد."
        )
        return response

    def form_invalid(self, form):
        messages.error(self.request, "ورود انجام نشد.")
        return super().form_invalid(form)

# class UserLoginView(LoginView):
#     form_class = UserLoginForms
#     template_name = 'login.html'
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         login(self.request , self.object)
#         messages.success(self.request,f'کاربر {self.object.first_name} با موفقیت وارد شد.')
#         return response
    
#     def form_invalid(self, form):
#         messages.error(self.request,'ثبت انجام نشد.')
#         return super().form_invalid(form)


def user_logout_view(request):
    logout(request)
    return redirect('home')

class UserLogOutView(LogoutView):
    next_page = 'home'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request,'کاربر با موفیقت خارج شد.')
        return super().dispatch(request, *args, **kwargs)   