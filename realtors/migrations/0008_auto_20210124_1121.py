# Generated by Django 3.1.5 on 2021-01-24 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0007_auto_20210124_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='phone',
            new_name='phone_number',
        ),
    ]