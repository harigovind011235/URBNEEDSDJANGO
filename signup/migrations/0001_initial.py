# Generated by Django 3.1.5 on 2021-01-14 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signuppro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_email', models.EmailField(default='nill', max_length=40)),
                ('pro_phn', models.IntegerField(default=32)),
                ('pro_profession', models.CharField(default='nill', max_length=30)),
                ('pro_experience', models.IntegerField(default=20)),
                ('pro_gender', models.CharField(default='nill', max_length=10)),
                ('pro_details', models.TextField(default='nill', max_length=50)),
                ('pro_documents', models.FileField(upload_to='documents/')),
                ('pro_username', models.CharField(default='nill', max_length=20)),
                ('pro_password', models.CharField(default='nill', max_length=20)),
                ('pro_password2', models.CharField(default='nill', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'SIGNUPPROFESSIONAL',
            },
        ),
    ]
