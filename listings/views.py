from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, sale_price_choices, province_choices, type_choices, status_choices_client, \
    rent_price_choices
from django.views import View
from realtors.models import Realtor
# Create your views here.
class ListingsView(View):
    def get(self,request):
        listings = Listing.objects.order_by('-list_date').filter(is_published=True, status__in=['For Rent', 'For Sale'])
        paginator = Paginator(listings, 6)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        context = {
            "listings": paged_listings
        }

        return render(request, "listings/listings.html", context)

class ListingView(View):
    def get(self,request, listing_id):
        listing = get_object_or_404(Listing, pk=listing_id)
        context = {
            'listing': listing
        }
        return render(request, "listings/listing.html", context)

class SearchView(View):
    def get(self,request):
        query_set = Listing.objects.order_by('-list_date').filter(is_published=True, status__in=['For Rent', 'For Sale'])
        realtors = Realtor.objects.all()
        if 'keywords' in request.GET:
            keyword = request.GET['keywords']
            if keyword:
                query_set = query_set.filter(description__icontains=keyword)
        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                query_set = query_set.filter(city__iexact=city)
        if 'province' in request.GET:
            state = request.GET['province']
            if state:
                query_set = query_set.filter(province__iexact=state)
        if 'sale_price' in request.GET:
            sale_price = request.GET['sale_price']
            if sale_price == '900001':
                query_set = query_set.filter(price__gte=sale_price)
            else:
                query_set = query_set.filter(price__lte=sale_price)
        if 'bedrooms' in request.GET:
            bedrooms = request.GET['bedrooms']
            if bedrooms:
                query_set = query_set.filter(bedrooms__iexact=bedrooms)
        if 'rent_price' in request.GET:
            rent_price = request.GET['rent_price']
            if rent_price == '9001':
                query_set = query_set.filter(price__gte=rent_price)
            else:
                query_set = query_set.filter(price__lte=rent_price)
        if 'type' in request.GET:
            type = request.GET['type']
            if type:
                query_set = query_set.filter(type__iexact=type)
        if 'status' in request.GET:
            status = request.GET['status']
            if status:
                query_set = query_set.filter(status__iexact=status)
        if 'area' in request.GET:
            area = request.GET['area']
            if area:
                query_set = query_set.filter(area__iexact=area)
        if 'realtor' in request.GET:
            realtor = request.GET.get('realtor')
            if realtor:
                query_set = query_set.filter(realtor__name=realtor)
        paginator = Paginator(query_set, 6)
        page = request.GET.get('page')
        paged_listings = paginator.get_page(page)
        context = {
            "bedroom_choices": bedroom_choices,
            "sale_price": sale_price_choices,
            "province_choices": province_choices,
            "type_choices": type_choices,
            "status_choices": status_choices_client,
            "rent_price": rent_price_choices,
            "values":request.GET,
            "listings":paged_listings,
            "realtors":realtors,
        }
        return render(request, "listings/search.html", context)
