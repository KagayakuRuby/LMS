from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
    context = {
        "username" : "Mohsen",
        "skills" : ["python","django","html"]
    }
    return render(request,'portfolio.html',context)

def article_id(request,article_id):
    return HttpResponse(f"article_id: {article_id}")

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'{name} دریافت شد.')
    return render(request,'contactus.html')