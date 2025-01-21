from django.shortcuts import render, redirect
from app.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
# from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required(login_url='/login/') 
def index(request):
    print(request.user)
    # if not request.user.is_authenticated:
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        # password = request.POST.get('name')
        contact = Contact(name=name, email=email, phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, "Message sent successfully.")
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    print("Before logout:", request.session)
    logout(request)
    print("After logout:", request.session)
    messages.success(request, "Logged out successfully.")
    return redirect("/login")