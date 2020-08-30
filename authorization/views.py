from django.shortcuts import render

# -------------------------------------------------------------------------
# for all views:

# who can access:
    # --> eveyone
# what i need:
    # a list of all the jobs (cashier, administration, analyst)
    # login-data to check wether the input is correct or not


# -------------------------------------------------------------------------
# views:

def authorization_login_view(request, *args, **kwargs):
    return render(request, "authorization_login.html", {})

def authorization_register_view(request, *args, **kwargs):
    return render(request, "authorization_register.html", {})

def authorization_forgot_password_view(request, *args, **kwargs):
    return render(request, "authorization_forgot_password.html", {})

def authorization_change_password_view(request, *args, **kwargs):
    return render(request, "authorization_change_password.html", {})
