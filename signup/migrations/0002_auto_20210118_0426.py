# Generated by Django 3.1.5 on 2021-01-18 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='signupclient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='signuppro',
            options={},
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_details',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_documents',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_email',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_experience',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_gender',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_password',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_password2',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_phn',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_profession',
        ),
        migrations.RemoveField(
            model_name='signuppro',
            name='pro_username',
        ),
    ]