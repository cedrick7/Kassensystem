from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
        'groups',
        'is_active',
        ]

class ChangePasswordForm(forms.Form):
    username = forms.CharField(max_length=150) 
    password = forms.CharField(max_length=150, widget=forms.PasswordInput) 
       


# class UserModelForm(form.Model):
#     class = Meta


####################################################################################################################


# copied from authorization.css
# styling = "display: block; width: 90%; height: 42px !important; padding: 10px; border: 1px solid #dfdfdf; " \
#           "border-radius: 5px; border-left: 0; border-top-left-radius: 0; border-bottom-left-radius: 0; " \
#           "-webkit-appearance: none; -moz-appearance: none; -ms-appearance: none; -o-appearance: none; appearance: none;"

# choices u can select as role
# choices = (
#     ('cashier', 'Kassierer'),
#     ('admin', 'Administrator'),
#     ('analyst', 'Analyst')
# )


# Login
# class FormLogin(forms.Form):
#     role = forms.ChoiceField(
#         required=True,
#         label='Rolle auswählen',
#         choices=choices,
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )

#     userid = forms.IntegerField(
#         required=True,
#         label='User-ID',
#         widget=forms.TextInput(
#             attrs={"placeholder": "User-ID",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password = forms.CharField(
#         required=True,
#         label='Password',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Password",
#                    "class": "inp4ut-group-item form-control needs-validation",
#                    "style": styling})
#     )

#     class Meta:
#         model = Employee
#         fields = ['userid', 'password', 'role']


# Registrieren
# class FormRegister(forms.Form):
#     role = forms.ChoiceField(
#         required=True,
#         label='Rolle auswählen',
#         choices=choices,
#         widget=forms.Select(
#             attrs={
#                 'class': 'form-control'
#             }
#         )
#     )
#     firstname = forms.CharField(
#         required=True,
#         label='Vorname',
#         widget=forms.TextInput(
#             attrs={"placeholder": "Vorname",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     lastname = forms.CharField(
#         required=True,
#         label='Nachname',
#         widget=forms.TextInput(
#             attrs={"placeholder": "Nachname",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password = forms.CharField(
#         required=True,
#         label='Password',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Password",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password_confirm = forms.CharField(
#         required=True,
#         label='Password',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Password",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     img = forms.FileField(
#         required=False,
#         label='Profilbild',
#         widget=forms.FileInput(
#             attrs={"placeholder": "Profilbild",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )

#     class Meta:
#         model = Employee
#         fields = ['role_choice', 'firstname', 'lastname', 'userid', 'password', 'password_confirm', 'img']


# Passwort vergessen
# class FormForgotPassword(forms.Form):
#     userid = forms.IntegerField(
#         required=True,
#         label='User-ID',
#         widget=forms.TextInput(
#             attrs={"placeholder": "User-ID",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password_old = forms.CharField(
#         required=True,
#         label='Altes Password',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Altes Password",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password_new = forms.CharField(
#         required=True,
#         label='Neues Password',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Neues Password",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password_new_confirm = forms.CharField(
#         required=True,
#         label='Neues Password bestätigen',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Neues Password bestätigen",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )


# class Meta:
#     model = Employee
#     fields = ['userid', 'password_old', 'password_new', 'password_new_confirm']


# Passwort ändern
# class FormChangePassword(forms.Form):
#     userid = forms.IntegerField(
#         required=True,
#         label='User-ID',
#         widget=forms.TextInput(
#             attrs={"placeholder": "User-ID",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password_old = forms.CharField(
#         required=True,
#         label='Altes Password',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Altes Password",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password_new = forms.CharField(
#         required=True,
#         label='Neues Password',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Neues Password",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )
#     password_new_confirm = forms.CharField(
#         required=True,
#         label='Neues Password bestätigen',
#         widget=forms.PasswordInput(
#             attrs={"placeholder": "Neues Password bestätigen",
#                    "class": "input-group-item form-control needs-validation",
#                    "style": styling})
#     )

#     class Meta:
#         model = Employee
#         fields = ['userid', 'password_old', 'password_new', 'password_new_confirm']

# Notizen (bitte stehen lassen)
# {% for choice in form.fields.role_choice.choices %}
#  <option value="{{ choice.0 }}">{{ choice.1 }}</option>
# {% endfor %}


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
