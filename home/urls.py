from django.urls import path
from . import views


urlpatterns = [

    path('',views.home,name='home'),
    path('booked/',views.booked,name='booked'),
    path('service2/',views.service2,name='service2')

]