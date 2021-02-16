from django import forms





cities = [('selectyourcity','Select Your City'),('chennai','Chennai'),('kochi','Kochi'),('delhi','Delhi'),('mumbai','Mumbai')]
services = [('selectaservice','Select Your Mode Of Service'),('hairstylist','HairStylist'),('electrician','Electrician'),('cleaner','Cleaner'),('mechanic','Mechanic')]
timeslots = [('select your timeslot','Select Your Timeslot'),('9am-10am','9am-10am'),('10am-11am','10am-11am'),('11am-12pm','11am-12pm'),('12pm-1pm','12pm-1pm')]

class serviceform(forms.Form):



    city1 = forms.CharField(widget=forms.Select(choices=cities), required=True)
    service1 = forms.CharField(widget=forms.Select(choices=services), required=True)
    servicedesc1 = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Explain Your Need In Short'}))
    time1 = forms.CharField(widget=forms.Select(choices=timeslots), required=True)
    date1 = forms.DateField(required=True)
