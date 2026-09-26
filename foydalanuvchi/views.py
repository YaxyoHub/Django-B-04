from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import User_Register_Form

# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect(
            'home'
        )

    if request.method == 'POST':
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')

        user = authenticate(
            request,
            username=user_username,
            password=user_password
        )

        if not user:
            messages.error(
                request,
                'Login yoki parol xato!'
            )
            return redirect(
                'login'
            )
        else:
            messages.success(
                request,
                'Login muvaffaqiyatli!'
            )
            login(
                request,
                user
            )
            return redirect(
                'home'
            )

    return render(
        request,
        'foydalanuvchi/login.html'
    )

def register_view(request):
    if request.user.is_authenticated:
        return redirect(
            'home'
        )

    if request.method == 'POST':
        form = User_Register_Form(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                'Ro`yxatdan o`tish muvaffaqiyatli!')
            return redirect(
                'home'
            )
        else:
            messages.error(
                request,
                form.errors
            )
            return redirect(
                'register'
            )

    empty_form = User_Register_Form()
    return render(
        request,
        'foydalanuvchi/register.html',
        context={'form': empty_form}
    )

def logout_view(request):
    logout(request)
    return redirect(
        'login'
    )
