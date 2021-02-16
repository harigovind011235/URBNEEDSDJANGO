from django.db import models

# Create your models here.
class services(models.Model):



    city = models.CharField(max_length=30,default="nill")
    service = models.CharField(max_length=30, default="nill")
    servicedesc = models.TextField(max_length=50, default="nill")
    time = models.CharField(max_length=30, default="nill")
    date = models.DateField()




    def __str__(self):
        return self.service

    class Meta:
        verbose_name_plural="SERVICEMODEL"