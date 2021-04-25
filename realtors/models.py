from django.db import models
from datetime import datetime
from stdimage import StdImageField
from django.conf import settings
import os
from PIL import Image
# Create your models here.

class Realtor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200, default='Not-available')
    photo = StdImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50, default='n/a')
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
