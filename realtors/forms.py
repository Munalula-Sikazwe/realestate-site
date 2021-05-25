from django.forms import ModelForm
from .models import Realtor
from listings.models import Listing
from django.forms import HiddenInput

class RealtorForm(ModelForm):
    class Meta:
        model = Realtor
        fields = ['phone_number', 'description', 'photo']


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        exclude = ['is_published', 'list_date' ]
        widgets = {'realtor': HiddenInput()}
