from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'variable':'Thie is sent'
    }
    # return HttpResponse("Hello World!")
    return render(request, 'index.html',context)

def about(request):
    # return HttpResponse("About page")
    return render(request, 'about.html')
