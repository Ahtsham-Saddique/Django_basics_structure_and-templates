# import django.http from HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello,this is the Home page of Django")
    return render(request, 'website/index.html')

def contact(request):
    return render(request,'website/contact.html')

def about(request):
    return render(request,"website/about.html")