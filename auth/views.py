from django.shortcuts import render

# -------------------------------------------------------------------------
# for all views:

# who can access:
    # --> eveyone
# what i need:
    # a list of all the jobs (cashier, admin, analyst)
    # login-data to check wether the input is correct or not


# -------------------------------------------------------------------------
# views:

def auth_login_view(request, *args, **kwargs):
    return render(request, "auth_login.html", {})

def auth_register_view(request, *args, **kwargs):
    return render(request, "auth_register.html", {})

def auth_forgot_password_view(request, *args, **kwargs):
    return render(request, "auth_forgot_password.html", {})

def auth_change_password_view(request, *args, **kwargs):
    return render(request, "auth_change_password.html", {})
