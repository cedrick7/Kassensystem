
from django import forms
from .models import Employee

# copied from authorization.css
styling = "display: block; width: 90%; height: 42px !important; padding: 10px; border: 1px solid #dfdfdf; " \
          "border-radius: 5px; border-left: 0; border-top-left-radius: 0; border-bottom-left-radius: 0; "

# Login
class FormLogin(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        widget = forms.TextInput(
            attrs = {"placeholder": "Username",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {"placeholder": "Password",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )

    class Meta:
        model = Employee
        fields = ['username', 'password']


# Registrieren
class FormRegister(forms.Form):
    role_select = forms.Select(
        choices = (
            ('cashier', 'Kassierer'),
            ('admin',   'Administrator'),
            ('analyst', 'Analyst'))
    )
    firstname = forms.CharField(
        required = True,
        label = 'Vorname',
        widget = forms.TextInput(
            attrs = {"placeholder": "Vorname",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    lastname = forms.CharField(
        required = True,
        label = 'Nachname',
        widget = forms.TextInput(
            attrs = {"placeholder": "Nachname",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    email = forms.CharField(
        required = True,
        label = 'E-Mail',
        widget = forms.EmailInput(
            attrs = {"placeholder": "E-Mail",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling,
                     "aria-describedby": "emailHelp"})
    )
    username = forms.CharField(
        required = True,
        label = 'Username',
        widget = forms.TextInput(
            attrs = {"placeholder": "Username",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {"placeholder": "Password",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    password_confirm = forms.CharField(
        required = True,
        label = 'Password',
        widget = forms.PasswordInput(
            attrs = {"placeholder": "Password",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    img = forms.FileField(
        required = False,
        label = 'Profilbild',
        widget = forms.FileInput(
            attrs = {"placeholder": "Profilbild",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )

    class Meta:
        model = Employee
        fields = ['role_select', 'firstname', 'lastname', 'email', 'username', 'password', 'password_confirm', 'img']


# Passwort vergessen
class FormForgotPassword(forms.Form):
    firstname = forms.CharField(
        required = True,
        label = 'Vorname',
        widget = forms.TextInput(
            attrs = {"placeholder": "Vorname",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    lastname = forms.CharField(
        required = True,
        label = 'Nachname',
        widget = forms.TextInput(
            attrs = {"placeholder": "Nachname",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    username = forms.CharField(
        required = True,
        label = 'Username',
        widget = forms.TextInput(
            attrs = {"placeholder": "Username",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )

    class Meta:
        model = Employee
        fields = ['firstname', 'lastname', 'username']



# Passwort ändern
class FormChangePassword(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        widget = forms.TextInput(
            attrs = {"placeholder": "Username",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    password_old = forms.CharField(
        required = True,
        label = 'Altes Password',
        widget = forms.PasswordInput(
            attrs = {"placeholder": "Altes Password",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    password_new = forms.CharField(
        required = True,
        label = 'Neues Password',
        widget = forms.PasswordInput(
            attrs = {"placeholder": "Neues Password",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )
    password_new_confirm = forms.CharField(
        required = True,
        label = 'Neues Password bestätigen',
        widget = forms.PasswordInput(
            attrs = {"placeholder": "Neues Password bestätigen",
                     "class": "input-group-item form-control needs-validation",
                     "style": styling})
    )

    class Meta:
        model = Employee
        fields = ['username', 'password_old', 'password_new', 'password_new_confirm']














# irgendwas, was hier nicht reingehört
# Administrator erstellt, bearbeitet, löscht employee
# class employeeForm_employeeBearbeiten(forms.ModelForm):
#     class Meta:
#         model = employee
#         fields = [
#             'firstname', 
#             'lastname', 
#             'role', 
#             'password'
#         ]
