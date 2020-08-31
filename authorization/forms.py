from django import forms
from .models import Request, Employee


# Anfage um sein Passwort zu ändern
class FormResetPassword(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'employee',  # employee kennt seine employee-Nummer
            'password',
            'password'
        ]


# Anfrage für einen neuen employee
class FormEmployeeCreateEdit(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'firstname',
            'lastname',
            'role',
            'password'
            # type automaisch, username automatisch
            # Administrator erstellt, bearbeitet, löscht employee
        ]



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
    #class Meta:
        model = Employee
        username = forms.CharField(widget= forms.Textarea(attrs= {"class": "form-row"}))
        password = forms.CharField(widget= forms.Textarea(attrs= {"class": "form-row"}))





