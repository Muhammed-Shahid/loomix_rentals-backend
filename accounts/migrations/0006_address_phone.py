# Generated by Django 4.2.5 on 2023-10-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_address_address_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='phone',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]
