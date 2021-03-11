from django.db import models
from datetime import datetime
from PIL import Image
from django.urls import reverse
import os
from realtors.models import Realtor
from .choices import province_choices, type_choices, status_choices_realtor
from stdimage import StdImageField


# Create your models here.

class Listing(models.Model):
    BEDROOM_CHOICES = bedroom_choices = [(0, 0),
                                         (1, 1),
                                         (2, 2),
                                         (3, 3),
                                         (4, 4),
                                         (5, 5),
                                         (6, 6),
                                         (7, 7),
                                         (8, 8),
                                         (9, 9),
                                         (10, 10)]

    PROVINCE_CHOICES = list(province_choices.items())
    TYPE_CHOICES = list(type_choices.items())
    STATUS_CHOICES = list(status_choices_realtor.items())

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES, default='')
    address = models.CharField(max_length=200)
    area = models.CharField(max_length=200, default='N/A')
    district = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200, choices=PROVINCE_CHOICES, default='')
    zipcode = models.CharField(max_length=200, default='10101')
    description = models.TextField(blank=True)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='')
    price = models.IntegerField()
    bedrooms = models.IntegerField(choices=BEDROOM_CHOICES, default='')
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField(default='')
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, default='')
    photo_main = StdImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = StdImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = StdImageField(upload_to='photos/%Y/%m/%d/', )
    photo_3 = StdImageField(upload_to='photos/%Y/%m/%d/')
    photo_4 = StdImageField(upload_to='photos/%Y/%m/%d/')
    photo_5 = StdImageField(upload_to='photos/%Y/%m/%d/')
    photo_6 = StdImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        photos = (self.photo_main, self.photo_1, self.photo_2, self.photo_3, self.photo_4, self.photo_5, self.photo_6)
        SIZE = (600, 338)

        for photo in photos:
            if photo:
                current_photo = Image.open(photo.path)
                photo_resized = current_photo.resize(SIZE)
                photo_resized.save(photo.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('listing', args=[str(self.id), ])
