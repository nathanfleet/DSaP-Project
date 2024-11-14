from django.shortcuts import render, redirect
from django.http import HttpResponse
from .auth import register_user, authenticate_user, login_required

def home(request):
    if 'user_id' in request.session:
        return render(request, 'home.html')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        register_user(username, password)
        return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate_user(username, password)
        if user:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')

# test
@login_required
def protected_view(request):
    return HttpResponse("You are authenticated!")
