from django.shortcuts import render,redirect
from signup.models import signuppro,signupclient
from .forms import professionalform,customerform
from django.http import HttpResponse
from signin.forms import signinform


# Create your views here.

def pro(request):

    if request.method == 'POST':
        form = professionalform(request.POST,request.FILES)

        if form.is_valid():

            email2 = form.cleaned_data['email1']
            tele2 = form.cleaned_data['tele1']
            pro2 = form.cleaned_data['pro1']
            exp2 = form.cleaned_data['experience1']
            gender2 = form.cleaned_data['gender1']
            desp2 = form.cleaned_data['description1']
            myfile2 = form.cleaned_data['myfile1']
            username2 = form.cleaned_data['username1']
            password2 = form.cleaned_data['password1']
            confirmpassword2 = form.cleaned_data['confirmpassword1']

            pro = signuppro()
            pro.pro_email = email2
            pro.pro_phn = tele2
            pro.pro_profession = pro2
            pro.pro_experience = exp2
            pro.pro_gender = gender2
            pro.pro_details = desp2
            pro.pro_documents = myfile2
            pro.pro_username= username2
            pro.pro_password = password2
            pro.pro_password2 = confirmpassword2

            pro.save()

            return HttpResponse("success")

    else:

        form = professionalform()
        return render(request,'signup/register1.html',{'form':form})


def customer(request):
    if request.method == 'POST':
        form = customerform(request.POST)



        if form.is_valid():
            email3 = form.cleaned_data['clientemail1']
            tele3 = form.cleaned_data['clienttele1']
            username3 = form.cleaned_data['clientusername1']
            password3 = form.cleaned_data['clientpassword1']
            confirmpassword3 = form.cleaned_data['clientconfirmpassword1']




            client = signupclient()
            client.client_email = email3
            client.client_phn = tele3
            client.client_username= username3
            client.client_password = password3
            client.client_password2 = confirmpassword3

            client.save()

            return redirect('signin')

    else:

        form = customerform()
        return render(request,'signup/register2.html',{'form':form})



