
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import *
from django.shortcuts import render, redirect


def register(request):
    if request.user.is_authenticated():
        return redirect('account')
    return redirect('/register/success')


def log_in(request):
    if request.user.is_authenticated():
        return redirect('account')

    return render(request, "log_in.html", {})


def log_out(request):
    logout(request)
    return redirect(log_in)
