from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator
from listings.choices import bedroom_choices, sale_price_choices, province_choices, type_choices, status_choices_client, \
    rent_price_choices


# Create your views here.

def home(request):
    ### Ichikulwa's landing page
    listings = Listing.objects.order_by('-list_date').filter(is_published=True, status__in=['For Rent', 'For Sale'])
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings,
        "bedroom_choices": bedroom_choices,
        "sale_price": sale_price_choices,
        "state_choices": province_choices,
        "type_choices": type_choices,
        "status_choices": status_choices_client,
        "rent_price": rent_price_choices

    }

    return render(request, 'pages/index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('hire_date')
    paginator = Paginator(realtors, 3)
    page = request.GET.get('page')
    paged_realtors = paginator.get_page(page)
    # mvp = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': paged_realtors,
        # 'mvp': mvp
    }
    return render(request, 'pages/about.html', context)
