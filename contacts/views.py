from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.views import View
from django.views.decorators.http import  require_POST
# Create your views here.
class ContactView(View):
    def post(self,request):
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id).exists()
            if has_contacted:
                messages.error(request, "An enquiry on this listing has already been made")
                return redirect('/listings/' + listing_id)
            else:
                contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)
                contact.save()
                messages.success(request,"Thankyou for your inquiry we'll respond , as soon as we can")


        return redirect('/listings/' + listing_id)
