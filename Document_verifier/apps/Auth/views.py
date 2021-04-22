
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from rest_framework import viewsets

from .models import User
from .forms import UserForm

# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        # Check if the form is valid
        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,
        'Auth/register.html',
        {'user_form': user_form,
        'registered': registered}
    )

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is not active")
        else:
            print(f"Invalid {email} {password}")
            return HttpResponse("Bad login credentials!")
    else:
        return render(
            request,
            'Auth/login.html',
            {}
        )

def profile(request):
    if request.user.is_authenticated:
        email = request.user.email
        return HttpResponse("This is the")
