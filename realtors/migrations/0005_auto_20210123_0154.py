# Generated by Django 3.1.5 on 2021-01-22 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_auto_20210123_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
