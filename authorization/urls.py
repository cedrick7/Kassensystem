from django.urls import path
from authorization.decorators import allowed_user
from .views import (
        registerUser,
        loginUser,
        logoutUser,
        passwordReset,
        RequestListView,
        RequestDeleteView,
        RequestAcceptView,
        AccountsListView,
        AccountsDeleteView
        
)

app_name =  'authorization'
urlpatterns=[
    path('login', loginUser, name='login'),
    path('register', registerUser, name='register'),
    path('logout', logoutUser, name='logout'),
    path('reset', passwordReset, name='reset'),
    path('Mitarbeiter', allowed_user(allowed_roles=['Administratoren'])(AccountsListView.as_view()), name='mitarbeiter'),
    path('<int:id>/delete', allowed_user(allowed_roles=['Administratoren'])(AccountsDeleteView.as_view()), name='delete_user'),
    path('request', allowed_user(allowed_roles=['Administratoren'])(RequestListView.as_view()), name='request'),
    path('<str:username>/<str:type>/delete', allowed_user(allowed_roles=['Administratoren'])(RequestDeleteView.as_view()), name='delete'),
    path('<str:username>/<str:type>/accept', allowed_user(allowed_roles=['Administratoren'])(RequestAcceptView.as_view()), name='accept')
    # path('Passwort_vergessen/', authorization_forgot_password_view, name='forgot-password'),
    # path('Passwort_ändern/', authorization_change_password_view, name='change-password'),
]