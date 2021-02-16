from django.shortcuts import render,redirect
from .forms import serviceform
from home.models import services
from signin.forms import signinform


# Create your views here.



def home(request):

    if request.method =='POST':

        return redirect('signin')

    else:
        x = request.session.get('name')
        print(x)
        request.session['name'] = "logout"
        if request.session['name'] != None:
            del request.session['name']


        form = serviceform()
        return render(request,'home/index.html',{'form':form})




def service2(request):

    if request.method == "POST":
        form = serviceform(request.POST)

        if form.is_valid():


            city2 = form.cleaned_data['city1']
            service2 = form.cleaned_data['service1']
            servicedesc2 = form.cleaned_data['servicedesc1']
            time2 = form.cleaned_data['time1']
            date2 = form.cleaned_data['date1']

            s = services()
            s.city = city2
            s.service = service2
            s.servicedesc = servicedesc2
            s.time = time2
            s.date = date2

            s.save()

            return render(request,'home/success.html')

    else:

        form = serviceform()

        return render(request,'home/index2.html',{'form':form})


def booked(request):
    return render(request,'home/success.html')