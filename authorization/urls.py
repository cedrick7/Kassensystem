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
        
)

app_name =  'authorization'
urlpatterns=[
    path('login', loginUser, name='login'),
    path('register', registerUser, name='register'),
    path('logout', logoutUser, name='logout'),
    path('reset', passwordReset, name='reset'),
    path('request', allowed_user(allowed_roles=['Administratoren'])(RequestListView.as_view()), name='request'),
    path('<str:username>/<str:type>/delete', allowed_user(allowed_roles=['Administratoren'])(RequestDeleteView.as_view()), name='delete'),
    path('<str:username>/<str:type>/accept', allowed_user(allowed_roles=['Administratoren'])(RequestAcceptView.as_view()), name='accept')
    # path('Passwort_vergessen/', authorization_forgot_password_view, name='forgot-password'),
    # path('Passwort_ändern/', authorization_change_password_view, name='change-password'),
]