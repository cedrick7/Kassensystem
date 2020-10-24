from django.urls import path
from .views import (
        LoginView,
        registerUser,
        
)

app_name =  'authorization'
urlpatterns=[
    path('', LoginView, name='login'),
    path('register', registerUser, name='register'),
    # path('Passwort_vergessen/', authorization_forgot_password_view, name='forgot-password'),
    # path('Passwort_ändern/', authorization_change_password_view, name='change-password'),
]

    