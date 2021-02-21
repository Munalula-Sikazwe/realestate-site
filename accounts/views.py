from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from realtors.models import Realtor
from realtors.forms import RealtorForm
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from listings.models import Listing
from django.urls import reverse_lazy, reverse


# Create your views here.
class TenantDashboardView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('/admin/')
            elif Realtor.objects.filter(user=request.user).exists():
                return redirect('realtor_dashboard')
            else:
                user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
                listings = Listing.objects.order_by('-list_date')
                context = {
                    'contacts': user_contacts,
                    'listings': listings
                }

                return render(request, 'accounts/tenant_dashboard.html', context)


class RealtorDashboardView(LoginRequiredMixin, View):

    def get(self, request):
        realtor = Realtor.objects.get(user=request.user)
        listings = Listing.objects.filter(realtor=realtor)
        context = {
            'listings': listings,
            'realtor': realtor
        }
        return render(request, 'accounts/realtor_dashboard.html', context)


class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user)

        if user:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            if request.user.is_staff:
                return redirect('/admin/')
            elif Realtor.objects.filter(user=request.user).exists():
                return redirect('realtor_dashboard')
            else:
                return redirect('tenant_dashboard')
        else:
            messages.error(request, "Please enter a correct username or password")
            return redirect('login')

    def get(self, request):
        return render(request, 'accounts/login.html')


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('home')


class RegisterView(TemplateView):
    def get(self, request):
        return render(request, 'accounts/choose_registration.html')


class TenantRegistrationView(View):
    def post(self, request):
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
                    user.save()
                    messages.success(request, 'Registration Successful  , You may now log in')
                    auth.login(request, user)
                    return redirect('tenant_dashboard')
        else:
            messages.error(request, 'The Passwords Did not Match')
            return redirect('tenant_registration')

    def get(self, request):
        return render(request, 'accounts/tenant_register.html')


#
class RealtorRegistrationView(View):
    def post(self, request):
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
                    user.save()
                    realtor = Realtor.objects.create(user=user, name=user.get_full_name(), email=user.email)
                    realtor.save()
                    messages.success(request, 'Almost Done, Add a photo and description')
                    auth.login(request, user)
                    return redirect('realtor_registration_phase2')
        else:
            messages.error(request, 'The Passwords Did not Match')
            return redirect('realtor_registration')

    def get(self, request):
        return render(request, 'accounts/realtor_register.html')


class RealtorRegistrationPhase2View(View):
    def post(self, request):
        realtor = Realtor.objects.get(user=request.user)
        realtor_form = RealtorForm(request.POST or None, request.FILES or None, instance=realtor)
        if realtor_form.is_valid():
            realtor_form.save()
            return redirect('realtor_dashboard')
        else:
            messages.error(request, 'Registration Error')
            realtor = Realtor.objects.get(user=request.user)
            realtor_form = RealtorForm(instance=realtor)
            context = {
                'form': realtor_form
            }
            return render(request, 'accounts/photo_submission_form.html', context)

    def get(self, request):
        realtor_form = RealtorForm()
        context = {
            'form': realtor_form
        }

        return render(request, 'accounts/photo_submission_form.html', context)


class CreateListingView(LoginRequiredMixin, CreateView):
    model = Listing
    template_name = 'accounts/createupdatelisting.html'
    fields = (
        'title', 'type', 'address', 'area', 'district', 'city', 'province', 'description', 'status', 'price',
        'bedrooms',
        'bathrooms', 'garage', 'sqft', 'lot_size', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5',
        'photo_6')

    def get_initial(self):
        realtor = Realtor.objects.get(user=self.request.user.pk)
        initial = super().get_initial()
        initial['realtor'] = realtor
        return initial

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        else:
            realtor = Realtor.objects.get(user=self.request.user.pk)
            return self.model.objects.filter(realtor=realtor)


class UpdateListingView(LoginRequiredMixin, UpdateView):
    model = Listing
    template_name = 'accounts/createupdatelisting.html'
    fields = ('title', 'type', 'address', 'area', 'district', 'city', 'province', 'description', 'status', 'price',
              'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size', 'photo_main', 'photo_1', 'photo_2', 'photo_3',
              'photo_4',
              'photo_5', 'photo_6')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        else:
            realtor = Realtor.objects.get(user=self.request.user.pk)
            return self.model.objects.filter(realtor=realtor)


class DeleteListingView(LoginRequiredMixin, DeleteView):
    model = Listing
    template_name = 'accounts/deletelisting.html'
    success_url = reverse_lazy('realtor_dashboard')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.model.objects.all()
        else:
            realtor = Realtor.objects.get(user=self.request.user.pk)
            return self.model.objects.filter(realtor=realtor)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Realtor
    fields = ('name', 'photo', 'description', 'phone_number', 'email')
    template_name = 'accounts/profile_update.html'

    def get_object(self):
        if self.request.user:
            return self.model.objects.get(user=self.request.user.pk)
