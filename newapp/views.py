from django.shortcuts import render, redirect, get_object_or_404
from newapp.models import Bus
from newapp.forms import BusForm


def bus_list(request):
    buses = Bus.objects.all()
    return render(request, "bus/bus_list.html", {"buses": buses})


def bus_create(request):
    form=BusForm()
    if request.method=='POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("bus_list")
    return render(request, "bus/bus_form.html", {"form": form})


def bus_update(request, id):
    bus = get_object_or_404(Bus, id=id)
    form = BusForm(request.POST or None, instance=bus)
    if form.is_valid():
        form.save()
        return redirect("bus_list")
    return render(request, "bus/bus_form.html", {"form": form})


def bus_delete(request, id):
    bus = get_object_or_404(Bus, id=id)
    bus.delete()
    return redirect("bus_list")
