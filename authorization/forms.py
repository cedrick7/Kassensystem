
from django import forms
from .models import Request, Employee


# Anfage um sein Passwort zu ändern
class FormResetPassword(forms.Form):
     model = Request
     employee = forms.IntegerField(blank=True, default=None) # employee kennt seine employee-Nummer
     password = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True,)
     passwordreenter = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True,)

       #Ready for styling


# Anfrage für einen neuen employee
class FormForgotPassword(forms.Form):
        model = Request
        firstname = forms.CharField(widget= forms.Charfield(attrs= {"class": "form-row"}))
        lastname = forms.CharField(widget= forms.CharField(attrs= {"class": "form-row"}))
        type = forms.CharField(
            max_length=2,
            choices="TYPE",
            blank=False, attrs= {"class": "form-row"})

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
        username = forms.CharField(widget= forms.CharField(attrs= {"class": "form-row"}))
        password = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True,)
#Form for /Login
#Ready for styling

class FormRegister(forms.Form):
    model = Employee
    username = forms.CharField(widget=forms.CharField(attrs={"class": "form-row"}))
    password = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True,)

    #Ready for styling
