from django.shortcuts import render
from .forms import *

# -------------------------------------------------------------------------
# for all views:

# who can access:
# --> eveyone
# what i need:
# login-data to check wether the input is correct or not


# -------------------------------------------------------------------------
# views:

def authorization_login_view(request, *args, **kwargs):
    login_form = FormLogin(request.POST or None)

    context = {
        'form': login_form
    }
    return render(request, "authorization_login.html", context)


def authorization_register_view(request, *args, **kwargs):
    register_form = FormLogin(request.POST or None)

    context = {
        'form': register_form
    }
    return render(request, "authorization_register.html", context)


def authorization_forgot_password_view(request, *args, **kwargs):
    forgot_password_form = FormLogin(request.POST or None)

    context = {
        'form': forgot_password_form
    }
    return render(request, "authorization_forgot_password.html", context)


def authorization_change_password_view(request, *args, **kwargs):
    change_password_form = FormChangePassword(request.POST or None)

    context = {
        'form': change_password_form
    }
    return render(request, "authorization_change_password.html", context)
