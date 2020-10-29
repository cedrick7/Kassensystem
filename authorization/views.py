from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, ChangePasswordForm, RequestForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.contrib.auth.hashers import make_password
from .models import Request, Active_Accounts
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import unauthenticated_user
from django.views.generic import (
    View,
    ListView,
    DeleteView,
)
import logging
logger = logging.getLogger('django')

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
    #create superuser if necessary
    # nicht implementiert

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

                # boolean values for request
                admn = False
                nlyst = False
                kssrr = False 
                for i in groups:
                    #add user to groups and set values for request
                    group = Group.objects.get(name=i)
                    tmp = str(group)
                    if tmp == 'Administratoren':
                        admn = True
                    elif tmp == 'Analysten':
                        nlyst = True
                    elif tmp == 'Kassierer':
                        kssrr = True
                    group.user_set.add(user)                      
                    #Django fügt nicht die Gruppen hinzu, deswegen manuell
                    messages.success(request,i)
                    
                ############################################
                #           request wird generiert         #
                ############################################
                usrnme = request.POST.get("username","")
                frstnm = request.POST.get("first_name","")
                lstnm = request.POST.get("last_name","")
                typ = 'AC'
                entry = Request.objects.create(username=usrnme, firstname=frstnm,lastname=lstnm, type=typ,admin=admn,kassierer=kssrr,analyst=nlyst)
                ############################################
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
                query_pr = Request.objects.filter(type='PR',username=username)
                query_ac = Request.objects.filter(type='AC',username=username)
                if query_pr.exists() or query_ac.exists():
                    messages.info(request, 'Es existiert bereits eine Anfrage')
                    return redirect('authorization:login')
                
                user.save(update_fields=['password'])
                messages.info(request, 'Passwort anfrage gesendet')
                # passwort geändert
                ############################################
                #           request wird generiert         #
                ############################################
                # usrnme = request.POST.get("username","")
                frstnm = user.first_name
                lstnm = user.last_name
                typ = 'PR'
                entry = Request.objects.create(username=username, firstname=frstnm,lastname=lstnm, type=typ)
                ############################################
                # set inactive
                user.is_active = False
                user.save(update_fields=['is_active'])
                return redirect('authorization:login')
            except:
                messages.info(request, 'Nutzer nicht vorhanden')
                form = ChangePasswordForm
                context = {
                'form':form
                }
                return render(request, "new/test_reset.html", context)
        else:
            form = ChangePasswordForm
            context = {
            'form':form
            }
            return render(request, "new/test_reset.html", context)
    else:
        form = ChangePasswordForm
        context = {
        'form':form
        }
        return render(request, "new/test_reset.html", context)

class RequestListView(LoginRequiredMixin,ListView):
    template_name = 'new/test_requests.html'
    queryset = Request.objects.all()

class RequestDeleteView(LoginRequiredMixin,View):
    template_name = 'new/test_delete.html'

    def get_object(self):
        username = self.kwargs.get("username")
        type = self.kwargs.get("type")
        obj = None
        if id is not None and type is not None:
            obj =  get_object_or_404(Request, username=username,type=type)
        return obj
   
    def get(self, request, username=None,type=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context = {
                "object":obj,
                "reaktion":"ablehnen"
            }
        return render(request, self.template_name, context)

    def post(self, request, username=None,type=None, *args, **kwargs): 
        context = {}    
        obj = self.get_object()
        if obj is not None:
            try:
                username = obj.username
                user = User.objects.get(username=username)
                # löschen des Accounts wenn Accountanfrage
                if type == 'AC':
                    user.delete()
                    logger.info('Nutzer wurde erfolgreich gelöscht')
                    # no Active_Account entry
                    obj.delete()
                    logger.info('Request wurde erfolgreich gelöscht')
                    return redirect('authorization:request')
                # löschen des Requests
                obj.delete()
                logger.info('Request wurde erfolgreich gelöscht')
                # Check if account is already registert
                query_aa = Active_Accounts.objects.filter(user=user)
                if query_aa.exists():
                    logger.info('Account ist bereits registriert')
                else:
                    entry = Active_Accounts(user=user)
                    entry.save()
                    logger.info('Account wurde registriert')
                return redirect('authorization:request')
            except:
                logger.info('Fehler beim löschen der Anfrage')
                return redirect('authorization:request')
        return render(request, self.template_name, context)

class RequestAcceptView(LoginRequiredMixin,View):
    template_name = 'new/test_delete.html'

    def get_object(self):
        username = self.kwargs.get("username")
        type = self.kwargs.get("type")
        obj = None
        if id is not None and type is not None:
            obj =  get_object_or_404(Request, username=username,type=type)
        return obj
   
    def get(self, request, username=None,type=None, *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context = {
            "object":obj,
            "reaktion": "annehmen"
        }
        return render(request, self.template_name, context)

    def post(self, request, username=None,type=None, *args, **kwargs): 
        context = {}    
        obj = self.get_object()
        if obj is not None:
            # Nutzer wird aktiv
            try:
                username = obj.username
                user = User.objects.get(username=username)
                user.is_active = True
                user.save(update_fields=['is_active'])
                logger.info('Nutzer aktiv')
                # Anfrage wird gelöscht
                obj.delete()
                context[object] = None
                logger.info('Request wurde erfolgreich gelöscht')
                # Account wird registriert
                query_aa = Active_Accounts.objects.filter(user=user)
                if query_aa.exists():
                    logger.info('Account ist bereits registriert')
                else:
                    entry = Active_Accounts(user=user)
                    entry.save()
                    logger.info('Account wurde registriert')
                return redirect('authorization:request')
            except:
                logger.info('Nutzer nicht gefunden')
                return redirect('authorization:request')
        return render(request, self.template_name, context)

class AccountsListView(LoginRequiredMixin, View):
    template_name = "new/administration_employees.html"

    def get(self,request, *args,**kwargs):
        queryset = Active_Accounts.objects.all()
        context = {
            'object_list':queryset
        }
        return render(request, self.template_name, context)

class AccountsDeleteView(LoginRequiredMixin, View):
    template_name = "new/test_delete_user.html"
    def get_object_aa(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Active_Accounts, user=id)
        return obj
    
    def get_object_ua(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(User, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        obj = self.get_object_aa()
        if obj is not None:
            context = {
                'object':obj
            }
        return render(request,self.template_name ,context)

    def post(self, request, id=None, *args, **kwargs):
        context = {}
        obj_aa = self.get_object_aa()
        obj_ua = self.get_object_ua()
        if obj_aa is not None and obj_ua is not None:
            obj_aa.delete()
            obj_ua.delete()
            context = {
                "object":None
            }
            return redirect('authorization:mitarbeiter')
        return render(request, self.template_name, context)

    
