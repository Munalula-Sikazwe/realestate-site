# from django.contrib.sitemaps import Sitemap
# from django.urls import reverse
#
# from listings.models import Listing
#
# class ListingsSiteMap(Sitemap):
#     def items(self):
#         return Listing.objects.all()
# class StaticPagesSiteMap(Sitemap):
#     def items(self):
#         return ['about','home','listings']
#     def location(self, items):
#         return reverse(items)