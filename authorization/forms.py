
from django import forms
from .models import Request, Employee


# Anfage um sein Passwort zu ändern
class FormResetPassword(forms.Form):
        model = Request
        employee = forms.CharField() # employee kennt seine employee-Nummer
        oldpassword = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-row"}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-row"}))
        passwordreenter = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-row"}))

       #Ready for styling


# Anfrage für einen neuen employee


class FormForgotPassword(forms.Form):
        model = Request
        firstname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
        lastname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
        username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
        type = forms.CharField()

            # type automatisch
            #Ready for styling




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

# employee LogIn


class FormLogin(forms.Form):

        model = Employee
        username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
        password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-row"}))
#Form for /Login
#Ready for styling

class FormRegister(forms.Form):
    model = Employee
    firstname = forms.CharField(max_length=45)
    lastname = forms.CharField(max_length=45)
    emailadress = forms.EmailField()
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-row"}))
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-row"}))
    picture = forms.FileField()
    role = forms.CharField()

    #Ready for styling
