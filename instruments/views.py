from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from .models import Instrument
from .forms import InstrumentForm
from drivers.manager import DriverManager
from measurements.models import Measurement

def instrument_list(request):
    instruments = Instrument.objects.all()

    return render(request, "instruments/list.html", {
        "instruments": instruments
    })

def instrument_detail(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk
    )

    measurements = instrument.measurements.all()[:10]

    return render(
        request,
        "instruments/detail.html",
        {
            "instrument": instrument,
            "measurements": measurements
        }
    )

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

def instrument_connect(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk
    )

    driver = DriverManager.get_driver(instrument)

    try:
        driver.connect()

        messages.success(
            request,
            f"{instrument.name} connected"
        )

    except Exception as e:

        messages.error(
            request,
            f"Connection failed: {e}"
        )

    return redirect(
        "instrument_detail",
        pk=instrument.pk
    )

def instrument_identify(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk
    )

    driver = DriverManager.get_driver(instrument)

    try:

        identity = driver.identify()

        messages.info(
            request,
            identity
        )

    except Exception as e:

        messages.error(
            request,
            f"Identify failed: {e}"
        )

    return redirect(
        "instrument_detail",
        pk=instrument.pk
    )

def instrument_measure(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk
    )

    driver = DriverManager.get_driver(instrument)

    try:
        driver.connect()

        result = driver.measure()

        Measurement.objects.create(
            instrument=instrument,
            function=result["function"],
            value=result["value"],
            unit=result["unit"],
        )

        messages.success(
            request,
            f'Measurement: {result["value"]} {result["unit"]}'
        )

    except Exception as e:

        messages.error(
            request,
            f"Measurement failed: {e}"
        )

    return redirect(
        "instrument_detail",
        pk=instrument.pk
    )