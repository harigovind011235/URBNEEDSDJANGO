from django.urls import path

from . import views


urlpatterns = [

    path('professional/',views.pro,name='pro'),
    path('customer/',views.customer,name='customer'),

]