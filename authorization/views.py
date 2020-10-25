from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
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

# def LoginView(request, *args, **kwargs):
#     template_name = 'authorization_login.html'
#     login_form = FormLogin(request.POST or None)

#     context = {
#         'form': login_form
#     }
#     return render(request, "authorization_login.html", context)                                               


# Registrieren
@unauthenticated_user
def registerUser(request, *args, **kwargs):
    context = {}
    admin_group, created = Group.objects.get_or_create(name='Administratoren')
    cashier_group, created = Group.objects.get_or_create(name='Kassierer')
    analyst_group, created = Group.objects.get_or_create(name='Analysten')

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data.get('groups')
            if not group:
                form = CreateUserForm()
                context = {'form':form}
                messages.info(request, 'Bitte mindestens eine Gruppe wählen')
                return render(request, "new/test_register.html", context)
            else:
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account wurde erstellt für ' + user + ' mit Rechten für:')
                for i in group:
                    messages.success(request,i)
                return redirect('authorization:login')
        else:
            messages.info(request, 'Anlegen des Nutzers fehlgeschlagen')
            return redirect('authorization:register')
    else:
        form = CreateUserForm()
        context = {'form':form}
        return render(request, "new/test_register.html", context)

@unauthenticated_user
def loginUser(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("Anmeldung erfolgreich!")
            return redirect('administration:tax_list')
        else:
            messages.info(request, 'Nutzername und Passwort stimmen nicht überein')

    return render(request, "new/test_login.html", context)

def logoutUser(request, *args, **kwargs):
    logout(request)
    return redirect('authorization:login')

    
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
