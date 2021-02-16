from django.db import models

# Create your models here.

class signuppro(models.Model):

    pro_email = models.EmailField(max_length=40,default="nill")
    pro_phn = models.IntegerField(default=32)
    pro_profession = models.CharField(max_length=30,default="nill")
    pro_experience = models.IntegerField(default=20)
    pro_gender = models.CharField(max_length=10,default="nill")
    pro_details = models.TextField(max_length=50,default="nill")
    pro_documents = models.FileField(upload_to = 'documents/',default="")
    pro_username = models.CharField(max_length=20,default="nill")
    pro_password = models.CharField(max_length=20,default="nill")
    pro_password2 = models.CharField(max_length=20,default="nill")


    def __str__(self):
        return self.pro_email

    class Meta:
        verbose_name_plural="SIGNUPPROFESSIONAL"



class signupclient(models.Model):
    client_email = models.EmailField(max_length=40, default="nill")
    client_phn = models.IntegerField(default=32)
    client_username = models.CharField(max_length=20, default="nill")
    client_password = models.CharField(max_length=20, default="nill")
    client_password2 = models.CharField(max_length=20, default="nill")


    def __str__(self):
        return self.client_email

    class Meta:
        verbose_name_plural="SIGNUPCUSTOMER"





