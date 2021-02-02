from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from realtors.models import Realtor
from realtors.form import RealtorForm, ListingForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def tenant_dashboard(request):
    if request.user.is_authenticated:
        ### check if user is in the realtor database and redirect appropriately
        if Realtor.objects.all().filter(name=request.user.get_full_name()).exists():
            return redirect('realtor_dashboard')
        else:
            user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
            context = {
                'contacts': user_contacts
            }

            return render(request, 'accounts/tenant_dashboard.html', context)


@login_required
def realtor_dashboard(request):
    if request.method == 'POST':
        realtor = Realtor.objects.get(name=request.user.get_full_name())
        listing_form = ListingForm(request.POST or None, request.FILES or None)
        if listing_form.is_valid():
            listing_details = listing_form.save(commit=False)
            listing_details.realtor = realtor
            listing_details.save()
            return redirect('realtor_dashboard')
        else:
            messages.error(request, 'The form is invalid')
            context = {
                'form': listing_form
            }
            return render(request, 'accounts/realtor_dashboard.html', context)
    else:
        listing_form = ListingForm()
        context = {
            'form': listing_form
        }
        return render(request, 'accounts/realtor_dashboard.html', context)
    return render(request, 'accounts/realtor_dashboard.html')

    return render(request, 'accounts/realtor_dashboard.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            if Realtor.objects.all().filter(name=user).exists():
                return redirect('realtor_dashboard')
            else:
                return redirect('tenant_dashboard')
    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('home')


def register(request):
    return render(request, 'accounts/choose_registration.html')


def tenant_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username you entered is already taken, please try another username.')
                return redirect('tenant_registration')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email you entered is already in use.Please try another')
                    return redirect('tenant_registration')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)
                    # auth.login(request,user)
                    # messages.success(request,'Registration Successful , You are now logged in')
                    # return redirect('dashboard')
                    user.save()
                    messages.success(request, 'Registration Successful  , You may now log in')
                    auth.login(request, user)
                    return redirect('tenant_dashboard')
        else:
            messages.error(request, 'The Passwords Did not Match')
            return redirect('tenant_registration')
    return render(request, 'accounts/tenant_register.html')


def realtor_registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username you entered is already taken, please try another username.')
                return redirect('realtor_registration')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'The email you entered is already in use.Please try another')
                    return redirect('realtor_registration')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email,
                                                    first_name=first_name, last_name=last_name)

                    # auth.login(request,user)
                    # messages.success(request,'Registration Successful , You are now logged in')
                    # return redirect('dashboard')
                    user.save()
                    realtor = Realtor.objects.create(name=username, email=email)
                    realtor.save()
                    messages.success(request, 'Registration Successful  , You may now log in')
                    auth.login(request, user)
                    return redirect('realtor_registration_phase2')
        else:
            messages.error(request, 'The Passwords Did not Match')
            return redirect('realtor_registration')
    return render(request, 'accounts/realtor_register.html')


def realtor_registration_phase2(request):
    if request.method == 'POST':
        realtor = Realtor.objects.get(name=request.user.username)
        realtors = Realtor.objects.get(pk=realtor.id)
        realtor_form = RealtorForm(request.POST or None, request.FILES or None, instance=realtors)
        # print(realtor_form.is_multipart()) Form ImageField Debug data
        # print(realtor_form.is_valid())
        if realtor_form.is_valid():
            realtor_details = realtor_form.save(commit=False)
            realtor_details.name = request.user.get_full_name()
            realtor_details.save()
            return redirect('realtor_dashboard')
    else:
        messages.error(request, 'Form submission failed')
        realtor = Realtor.objects.get(name=request.user.username)
        realtors = Realtor.objects.get(pk=realtor.id)
        realtor_form = RealtorForm(instance=realtors)
        context = {
            'form': realtor_form
        }
        return render(request, 'accounts/photo_submission_form.html', context)
    return render(request, 'accounts/photo_submission_form.html')

# user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
# context = {
#     'contacts': user_contacts
# }
