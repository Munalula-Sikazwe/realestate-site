# Generated by Django 3.1.6 on 2021-02-17 15:19

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(default='N/A', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='lot_size',
            field=models.DecimalField(decimal_places=1, default='', max_digits=5),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=stdimage.models.JPEGField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=stdimage.models.JPEGField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=stdimage.models.JPEGField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=stdimage.models.JPEGField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=stdimage.models.JPEGField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=stdimage.models.JPEGField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=stdimage.models.JPEGField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='province',
            field=models.CharField(choices=[('Lusaka', 'Lusaka'), ('Western', 'Western'), ('Northern', 'Northern'), ('North-Western', 'North-Western'), ('Southern', 'Southern'), ('Luapula', 'Luapula'), ('Copperbelt', 'Copperbelt'), ('Muchinga', 'Muchinga'), ('Central', 'Central'), ('Eastern', 'Eastern')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('For Rent', 'For Rent'), ('For Sale', 'For Sale'), ('sold', 'sold'), ('rented', 'rented'), ('unavaliable', 'unavaliable')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Bedsitter', 'Bedsitter'), ('Commercial', 'Commercial'), ('Condo', 'Condo'), ('Cottage', 'Cottage'), ('Duplex', 'Duplex'), ('Flat', 'Flat'), ('Hotel', 'Hotel'), ('Incomplete House', 'Incomplete House'), ('Land', 'Land'), ('Lodge', 'Lodge'), ('Maisonette', 'Maisonette'), ('Man', 'Mansion'), ('Mansion', 'Multi Family Home'), ('Multi Storey', 'Multi Storey'), ('Office Space', 'Office Space'), ('Plot', 'Plot'), ('Ranch', 'Ranch'), ('Single Family Hom', 'Single Family Home'), ('Townhouse', 'Townhouse'), ('Unit', 'Unit'), ('Villa', 'Villa'), ('Warehouse', 'Warehouse')], default='', max_length=200),
        ),
    ]
