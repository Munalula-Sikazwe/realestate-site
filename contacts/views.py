from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail


# Create your views here.
def contact(request):
    if request.method == 'POST':
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
            has_contacted = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
            if has_contacted:
                messages.error(request, "An enquiry on this listing has already been made")
                return redirect('/listings/' + listing_id)
        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message,
                          user_id=user_id)
        contact.save()
        send_mail(
            'Property Listings Enquiry',
            'There has been an Enquiry for ' + listing + '. Sign into the your realtor account for more info',
            'ichikulwa@gmail.com',
            [realtor_email],
            fail_silently=True,
        )
        messages.success(request, "Thankyou for you enquiry , We'll respond shortly")

        return redirect('/listings/' + listing_id)
