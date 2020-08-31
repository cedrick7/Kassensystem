from django import forms
from .models import Request, Employee


# Anfage um sein Passwort zu ändern
class Form_Reset_Password(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'employee', # employee kennt seine employee-Nummer 
            'password', 
            'password'
        ]

# Anfrage für einen neuen employee
class Form_Employee_Create_Tweak(forms.ModelForm):
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
class Form_Login(forms.ModelForm):
    
    employeeID = forms.IntegerField()
    # pw = employee.password
    class Meta:
        model = Employee
        fields = [
            
            'password', 
            # employee meldet sich an
        ] 