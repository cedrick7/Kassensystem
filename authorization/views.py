from django.shortcuts import render
from .forms import FormLogin

# -------------------------------------------------------------------------
# for all views:

# who can access:
# --> eveyone
# what i need:
# login-data to check wether the input is correct or not


# -------------------------------------------------------------------------
# views:

def authorization_login_view(request, *args, **kwargs):
    return render(request, "authorization_login.html", {})


def authorization_register_view(request, *args, **kwargs):
    form = FormLogin(request.POST or None)

    context = {
        'form': form

    }
    return render(request, "authorization_register.html", context)


def authorization_forgot_password_view(request, *args, **kwargs):
    return render(request, "authorization_forgot_password.html", {})


def authorization_change_password_view(request, *args, **kwargs):
    return render(request, "authorization_change_password.html", {})
