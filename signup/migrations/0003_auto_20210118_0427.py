# Generated by Django 3.1.5 on 2021-01-18 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_auto_20210118_0426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signupclient',
            options={'verbose_name_plural': 'SIGNUPCUSTOMER'},
        ),
        migrations.AlterModelOptions(
            name='signuppro',
            options={'verbose_name_plural': 'SIGNUPPROFESSIONAL'},
        ),
        migrations.AddField(
            model_name='signupclient',
            name='client_email',
            field=models.EmailField(default='nill', max_length=40),
        ),
        migrations.AddField(
            model_name='signupclient',
            name='client_password',
            field=models.CharField(default='nill', max_length=20),
        ),
        migrations.AddField(
            model_name='signupclient',
            name='client_password2',
            field=models.CharField(default='nill', max_length=20),
        ),
        migrations.AddField(
            model_name='signupclient',
            name='client_phn',
            field=models.IntegerField(default=32),
        ),
        migrations.AddField(
            model_name='signupclient',
            name='client_username',
            field=models.CharField(default='nill', max_length=20),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_details',
            field=models.TextField(default='nill', max_length=50),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_documents',
            field=models.FileField(default='2', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_email',
            field=models.EmailField(default='nill', max_length=40),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_experience',
            field=models.IntegerField(default=20),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_gender',
            field=models.CharField(default='nill', max_length=10),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_password',
            field=models.CharField(default='nill', max_length=20),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_password2',
            field=models.CharField(default='nill', max_length=20),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_phn',
            field=models.IntegerField(default=32),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_profession',
            field=models.CharField(default='nill', max_length=30),
        ),
        migrations.AddField(
            model_name='signuppro',
            name='pro_username',
            field=models.CharField(default='nill', max_length=20),
        ),
    ]
