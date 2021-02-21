from django.db import models
from datetime import datetime
from stdimage import JPEGField
from django.conf import settings

# Create your models here.
class Realtor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200, default='Not-available')
    photo = JPEGField(upload_to="photos/%Y/%m/%d/", variations={
        'full': (200,200), 'thumbnail': (200, 200)
    })
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50, default='n/a')
    #is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
