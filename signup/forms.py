from django import forms

# Create your forms here.


jobs = [('hairdresser','HAIR DRESSER'),('plumber','PLUMBER'),('electrician','ELECTRICIAN'),('mechanic','MECHANIC'),('cleaningexpert','CLEANING EXPERT')]
gender = [('M', 'Male'), ('F', 'Female'),('other','OTHER')]

class professionalform(forms.Form):
    email1 = forms.EmailField(required = True)
    tele1 = forms.IntegerField(required = True)
    pro1 = forms.CharField(widget=forms.Select(choices=jobs), required=True)
    experience1 = forms.IntegerField(required = True)
    gender1 = forms.CharField(label='Gender',widget=forms.RadioSelect(choices=gender))
    description1 = forms.CharField(widget=forms.Textarea)
    myfile1 = forms.FileField()
    username1 = forms.CharField(max_length=20,required = True)
    password1 = forms.CharField(widget=forms.PasswordInput())
    confirmpassword1 = forms.CharField(widget=forms.PasswordInput())



class customerform(forms.Form):
    clientemail1 = forms.EmailField(required=True)
    clienttele1 = forms.IntegerField(required=True)
    clientusername1 = forms.CharField(required=True)
    clientpassword1 = forms.CharField(widget=forms.PasswordInput())
    clientconfirmpassword1 = forms.CharField(widget=forms.PasswordInput())

