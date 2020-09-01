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
    LoginForm = FormLogin(request.POST or None)

    context = {
        'form': LoginForm

    }
    return render(request, "authorization_login.html", context)


def authorization_register_view(request, *args, **kwargs):
    RegisterForm = FormLogin(request.POST or None)

    context = {
        'form': RegisterForm

    }
    return render(request, "authorization_register.html", context)


def authorization_forgot_password_view(request, *args, **kwargs):
    ForgotPasswordForm = FormLogin(request.POST or None)

    context = {
        'form': ForgotPasswordForm

    }
    return render(request, "authorization_forgot_password.html", {})


def authorization_change_password_view(request, *args, **kwargs):
    ResetPasswordForm = FormResetPassword(request.POST or None)

    context = {
        'form': ResetPasswordForm

    }
    return render(request, "authorization_change_password.html", context)
