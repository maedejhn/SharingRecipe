# Generated by Django 4.2.3 on 2023-07-31 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0005_chef_password2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='password2',
        ),
    ]
