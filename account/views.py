from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm
from django import forms
# from .models import User
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def signup_view(request):
    print('=================', request)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else: 
        form = UserCreationForm()
    # success_url = reverse_lazy("catalog")
    return render(request, 'signup.html', {'form': form})


def login_view(request): 
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login to admin user
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', { 'form': form })

def logout_view(request): 
    if request.method == 'POST' :
        logout(request)
        return redirect('index')