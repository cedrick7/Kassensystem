from django.urls import path
from .views import (
        LoginView,
        # authorization_register_view, 
        # authorization_forgot_password_view,
        # authorization_change_password_view
)

app_name =  'authorization'
urlpatterns=[
    path('', LoginView, name='login'),
    # path('Registrieren/', authorization_register_view, name='register'),
    # path('Passwort_vergessen/', authorization_forgot_password_view, name='forgot-password'),
    # path('Passwort_ändern/', authorization_change_password_view, name='change-password'),
]