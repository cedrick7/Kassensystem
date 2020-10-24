from django.shortcuts import render, redirect
from .forms import FormLogin, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    View,
)


# -------------------------------------------------------------------------
# for all views:

# who can access:
# --> eveyone
# what i need:
# login-data to check wether the input is correct or not


# -------------------------------------------------------------------------
# views:

def LoginView(request, *args, **kwargs):
    template_name = 'authorization_login.html'
    login_form = FormLogin(request.POST or None)

    context = {
        'form': login_form
    }
    return render(request, "authorization_login.html", context)


# Registrieren
def registerUser(request, *args, **kwargs):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authorization:login')

    context = {
        'form':form
    }

    return render(request, "new/authorization_register.html", context)
    
# def authorization_register_view(request, *args, **kwargs):
#     register_form = FormRegister(request.POST or None)

#     context = {
#         'form': register_form
#     }
#     return render(request, "authorization_register.html", context)


# def authorization_forgot_password_view(request, *args, **kwargs):
#     forgot_password_form = FormForgotPassword(request.POST or None)

#     context = {
#         'form': forgot_password_form
#     }
#     return render(request, "authorization_forgot_password.html", context)


# def authorization_change_password_view(request, *args, **kwargs):
#     change_password_form = FormChangePassword(request.POST or None)

#     context = {
#         'form': change_password_form
#     }
#     return render(request, "authorization_change_password.html", context)
