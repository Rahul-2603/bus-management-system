from django.shortcuts import render, redirect, get_object_or_404
from newapp.models import Bus
from newapp.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponse

def admin_check(user):
    return user.is_staff

@login_required
def bus_list(request):
    buses = Bus.objects.all()
    return render(request, "bus/bus_list.html", {"buses": buses})


@user_passes_test(admin_check)
def bus_create(request):
    form=BusForm()
    if request.method=='POST':
        form = BusForm(request.POST)
        
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect("bus_list")
        else:
            print(form.errors)
    return render(request, "bus/bus_form.html", {"form": form})

@user_passes_test(admin_check)
def bus_update(request, id):
    bus = get_object_or_404(Bus, id=id)
    form=BusForm()
    if request.method=='POST':
        form = BusForm(request.POST,instance=bus)
        if form.is_valid():
            form.save()
            return redirect("bus_list")
    return render(request, "bus/bus_form.html", {"form": form})


@user_passes_test(admin_check)
def bus_delete(request, id):
    bus = get_object_or_404(Bus, id=id)
    bus.delete()
    return redirect("bus_list")



def register(request):
    
    form=CustomUserCreationForm()
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    return render(request, 'registration/register.html', {'form': form})



from django.shortcuts import render, redirect

def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('bus_list')
        else:
            return redirect('search_bus')
            
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)
        if request.user.is_staff:
            print(user.is_staff)
            return redirect('bus_list')
        else:
            return redirect('search_bus')
       

    return render(request, 'registration/user_login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('user_login')


def search_bus(request):
    buses = None
    if request.GET:
        source = request.GET.get('source')
        destination = request.GET.get('destination')

        buses = Bus.objects.filter(
            source__iexact=source,
            destination__iexact=destination
        )

    return render(request, 'bus/search_bus.html', {'buses': buses})