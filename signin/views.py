from django.shortcuts import render,redirect
from .forms import signinform
from signup.models import signupclient
from django.http import HttpResponse
from home.forms import serviceform

# Create your views here.

def signin(request):

    if request.method == 'POST':
        form = signinform(request.POST)
        if form.is_valid():
            viewusername = form.cleaned_data['user_name']
            viewpassword = form.cleaned_data['password']
            if signupclient.objects.filter(client_username=viewusername).exists():
                user = signupclient.objects.get(client_username=viewusername)

                if user.client_password == viewpassword:
                    request.session['name'] = viewusername

                    return redirect('service2')

                else:
                    return HttpResponse("invalid username/password")

            else:
                form=signinform()
                return render(request,'signin/signin.html', {'form': form})

    else:

        form = signinform()
        return render(request,'signin/signin.html',{'form':form})


