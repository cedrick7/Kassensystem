from django.shortcuts import render, redirect
from .forms import CreateUserForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
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

    #create groups if necessary
    admin_group, created = Group.objects.get_or_create(name='Administratoren')
    cashier_group, created = Group.objects.get_or_create(name='Kassierer')
    analyst_group, created = Group.objects.get_or_create(name='Analysten')

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            groups = form.cleaned_data.get('groups')
            if not groups:
                #need of specifying a group
                form = CreateUserForm()
                context = {'form':form}
                messages.info(request, 'Bitte mindestens eine Gruppe wählen')
                return render(request, "new/test_register.html", context)
            else:
                #safe user
                form.save()
                username = form.cleaned_data.get('username')
                user = User.objects.get(username=username)
                messages.success(request, 'Account wurde erstellt für ' + username + ' mit Rechten für:')
                for i in groups:
                    #add user to groups
                    group = Group.objects.get(name=i)
                    group.user_set.add(user)                        #Django fügt nicht die Gruppen hinzu, deswegen manuell
                    messages.success(request,i)
                # set inactive
                user.is_active = False
                user.save(update_fields=['is_active'])
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
            groups = user.groups.all()
            count = groups.count()
            links = []
            if count > 1:
                if request.user.groups.filter(name = 'Administratoren').exists():
                   links.append("AD")
                
                if request.user.groups.filter(name = 'Kassierer').exists():
                    links.append('KA')

                if request.user.groups.filter(name = 'Analysten').exists():
                    links.append('AN')

                context = {'links':links}
                return render(request,'new/test_multigroup.html', context)

            # Weiterleitung auf Basis der Gruppe    
            else:
                if request.user.groups.filter(name = 'Administratoren').exists():
                    return redirect('administration:product_list')

                if request.user.groups.filter(name = 'Kassierer').exists():
                    return redirect('administration:cashbox_list')

                if request.user.groups.filter(name = 'Analysten').exists():
                    return redirect('administration:product_list')
        else:
            messages.info(request, 'Nutzername und Passwort stimmen nicht überein')

    return render(request, "new/test_login.html", context)

def logoutUser(request, *args, **kwargs):
    logout(request)
    return redirect('authorization:login')

@unauthenticated_user
def passwordReset(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                user = User.objects.get(username=username)
                password = make_password(form.cleaned_data['password'])
                user.password = password
                user.save(update_fields=['password'])
                messages.info(request, 'Passwort erfolgreich geändert')
                return redirect('authorization:login')
            except:
                messages.info(request, 'Nutzer nicht vorhanden')
                form = ChangePasswordForm
                context = {
                'form':form
        }
        else:
            form = ChangePasswordForm
            context = {
            'form':form
            }
    else:
        form = ChangePasswordForm
        context = {
            'form':form
        }
    return render(request, "new/test_reset.html", context)

def set_active(username):
    try:
        user = User.objects.get(username=username)
        user.is_active = True
        user.save(update_fields=['is_active'])
    except :
        messages.info("Nutzer konnte nicht aktiviert werden")
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
