# Generated by Django 4.2.3 on 2023-07-31 16:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0005_alter_food_raw_materials'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='chefs_of_food',
            field=models.ManyToManyField(related_query_name='chefs_of_food', to=settings.AUTH_USER_MODEL),
        ),
    ]
