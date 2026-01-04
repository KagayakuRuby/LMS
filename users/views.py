from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.views.generic import ListView,DetailView,FormView
from .forms import  *


def profile_list_view(request):
    profiles = Profile.objects.select_related('user')
    return render(request, 'profile_list.html', {'profiles': profiles})


class ProfileListVeiw(ListView):
    model = Profile
    queryset = Profile.objects.select_related('user')
    # queryset = Profile.objects.filter(role__exact='student')
    template_name = 'profile_list.html'
    context_object_name = 'profiles'


def profile_detail_view(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'profiles_detail.html', {'profile': profile})

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles_detail.html'
    context_object_name = 'profile'

def subscribe(request):
    if request.method == 'POST':
      form = UserForm(request.POST)
      if form.is_valid():
          email = form.cleaned_data['email']
          print('ثبت شد.',email)
    else:
        form = UserForm()
        print('no')
    return render(request,'subscribe.html',{'form':form})



class SubscribeView(FormView):
    template_name = 'subscribe.html'
    form_class = UserForm


    def form_valid(self, form):
        email = form.cleaned_data['email']
        print('ثبت شد.', email)
        return form().form_valid(form)

    def form_invalid(self, form):
        print('no')
        return form().form_invalid(form)