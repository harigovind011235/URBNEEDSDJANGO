from django import forms


class signinform(forms.Form):

    user_name = forms.CharField(required = True)
    password = forms.CharField(widget=forms.PasswordInput())
    rememberme = forms.BooleanField(required = True)