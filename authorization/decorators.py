from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            context = {}
            groups = request.user.groups.all()
            count = groups.count()
            links = []
            if count > 1:
                if request.user.groups.filter(name = 'Administratoren').exists():
                   links.append("Link zu Administrator")
                
                if request.user.groups.filter(name = 'Kassierer').exists():
                    links.append('Link zu Kassierer')

                if request.user.groups.filter(name = 'Analysten').exists():
                    links.append('Link zu Analyten')

                context = {'links':links}
                return render(request,'new/test_multigroup.html', context)

            # Weiterleitung auf Basis der Gruppe    
            else:
                if request.user.groups.filter(name = 'Administratoren').exists():
                    return redirect('administration:administration_dashboard')

                if request.user.groups.filter(name = 'Kassierer').exists():
                    return redirect('administration:cashbox_list')

                if request.user.groups.filter(name = 'Analysten').exists():
                    return redirect('administration:product_list')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
