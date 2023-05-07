from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.core.paginator import Paginator

from EV_chargers.settings import DEFAULT_FROM_EMAIL
from users.forms import UserCreationForm, UserUpdateForm
from EV_rent.models import RentalHistory


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            print(form)
            login(request, user)

            #РАБОТАЕТ, ПОТОМ ПЕРЕПИСАТЬ
            send_mail(subject='Successful Registration Message',
message= f"""
You have successfully registered on EV_Rent
Your login details:
===============================
    username: {username}
    password: {password}
===============================
""",
                      recipient_list=[email],
                      from_email=DEFAULT_FROM_EMAIL
                      )

            return redirect('home')



        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")

    rental_hst = RentalHistory.objects.filter(user=request.user).order_by('-id')
    paginator = Paginator(rental_hst, 5)
    page_number = request.GET.get('page')
    rental_hst = paginator.get_page(page_number)


    form = UserUpdateForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('profile')

    context = {
        "form": form,
        "rental_hst": rental_hst
    }

    return render(request, template_name="registration/profile.html", context=context)
