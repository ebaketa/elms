from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Instrument
from .forms import InstrumentForm

def instrument_list(request):
    instruments = Instrument.objects.all()

    return render(request, "instruments/list.html", {
        "instruments": instruments
    })

def instrument_detail(request, pk):
    instrument = get_object_or_404(Instrument, pk=pk)
    return render(request, "instruments/detail.html", {
        "instrument": instrument
    })

def instrument_create(request):
    if request.method == "POST":
        form = InstrumentForm(request.POST)
        if form.is_valid():
            instrument = form.save()
            return redirect("instrument_detail", pk=instrument.pk)
    else:
        form = InstrumentForm()

    return render(request, "instruments/form.html", {
        "form": form
    })

def instrument_edit(request, pk):
    instrument = get_object_or_404(Instrument, pk=pk)

    if request.method == "POST":
        form = InstrumentForm(request.POST, instance=instrument)
        if form.is_valid():
            form.save()
            return redirect("instrument_detail", pk=pk)
    else:
        form = InstrumentForm(instance=instrument)

    return render(request, "instruments/form.html", {
        "form": form,
        "instrument": instrument
    })

def instrument_delete(request, pk):
    instrument = get_object_or_404(Instrument, pk=pk)

    if request.method == "POST":
        instrument.delete()
        return redirect("instrument_list")

    return render(request, "instruments/delete.html", {
        "instrument": instrument
    })