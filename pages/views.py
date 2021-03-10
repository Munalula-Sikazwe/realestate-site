from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices, sale_price_choices, province_choices, type_choices, status_choices_client, \
    rent_price_choices
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class HomeView(View):
    def get(self,request):
        ### Ichikulwa's landing page
        listings = Listing.objects.order_by('-list_date').filter(is_published=True, status__in=['For Rent', 'For Sale'])[:3]
        realtors = Realtor.objects.all()
        context = {
            "listings": listings,
            "bedroom_choices": bedroom_choices,
            "sale_price": sale_price_choices,
            "state_choices": province_choices,
            "type_choices": type_choices,
            "status_choices": status_choices_client,
            "rent_price": rent_price_choices,
            "realtors":realtors

        }

        return render(request, 'pages/index.html', context)

class AboutView(TemplateView):
     template_name = 'pages/about.html'

