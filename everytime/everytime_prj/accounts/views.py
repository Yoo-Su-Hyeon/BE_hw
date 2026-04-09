from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'GET':
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})
    
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('posts:main')
    else:
        return render(request, 'signup.html', {'form':form})
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html',{'form': AuthenticationForm()})
    form =AuthenticationForm(request, request.POST)
    if form.is_valid():
        auth_login(request, form.user_cache)
        return redirect('posts:main')
    return render(request, 'login.html',{'form':form})

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('posts:main')

@login_required
def mypage(request):
    return render(request, 'mypage.html')

def user_info(request):
    return render(request, 'user_info.html')
