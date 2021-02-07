# from django.shortcuts import render, get_object_or_404
# from .models import Realtor
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from listings.models import Listing
#
#
# # Create your views here.
# def home(request):
#     realtors = Realtor.objects.order_by('-hire_date')
#     paginator = Paginator(realtors, 6)
#     page = request.GET.get('page')
#     paged_realtors = paginator.get_page(page)
#     context = {
#         'realtors': paged_realtors
#     }
#     return render(request, 'realtors/realtors.html', context)
#
#
# def listings(request, realtor_id):
#     realtor = get_object_or_404(Realtor, pk=realtor_id)
#     listings = Listing.objects.order_by('-list_date').filter(realtor=realtor)
#     paginator = Paginator(listings, 6)
#     page = request.GET.get('page')
#     paged_realtors = paginator.get_page(page)
#     context = {
#         'listings': paged_realtors
#     }
#     return render(request, 'listings/listings.html', context)
