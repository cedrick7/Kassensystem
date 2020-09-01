
from django import forms
from .models import Request, Employee


# Anfage um sein Passwort zu ändern
class FormResetPassword(forms.Form):
        model = Request
        employee = forms.CharField(blank=True) # employee kennt seine employee-Nummer
        oldpassword = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True)
        password = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True)
        passwordreenter = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True)

       #Ready for styling


# Anfrage für einen neuen employee
class FormForgotPassword(forms.Form):
        model = Request
        firstname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
        lastname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
        username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
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
        username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
        password = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True,)
#Form for /Login
#Ready for styling

class FormRegister(forms.Form):
    model = Employee
    firstname = forms.CharField(max_length=45, blank=False)
    lastname = forms.CharField(max_length=45, blank=False)
    emailadress = forms.EmailField(blank=False, widget=forms.CharField(attrs={"class": "form-row"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
    password = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True,)
    confirmpassword = forms.CharField(blank=False, widget=forms.PasswordInput(attrs={"class": "form-row"}), editable=True, )
    picture = forms.FileField(upload_to='mit_img/', default='static/mit_img/default.jpg', blank=True)
    role = forms.CharField(
        max_length=2,
        choices='PERMISSIONS',
        default='CASHIER',
        attrs={"class": "form-row"}
    )

    #Ready for styling
