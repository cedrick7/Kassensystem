from django.urls import path
from .views import (
        registerUser,
        loginUser,
        logoutUser
        
)

app_name =  'authorization'
urlpatterns=[
    path('login', loginUser, name='login'),
    path('register', registerUser, name='register'),
    path('logout', logoutUser, name='logout'),
    # path('Passwort_vergessen/', authorization_forgot_password_view, name='forgot-password'),
    # path('Passwort_ändern/', authorization_change_password_view, name='change-password'),
]

    