from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from .models import Instrument, InstrumentStatus, InstrumentCategory
from .forms import InstrumentForm
from drivers.manager import DriverManager
from measurements.models import Measurement
from django.utils import timezone
from django.db.models import Q
from services.connection_service import ConnectionService
from django.contrib import messages
from django.shortcuts import redirect
from services.instrument_service import InstrumentService

def instrument_connect(request, pk):

    instrument = get_object_or_404(Instrument, pk=pk)

    try:
        ConnectionService.connect(instrument)

        instrument.status = "online"
        instrument.save(update_fields=["status"])

        messages.success(
            request,
            f"{instrument.name} connected successfully."
        )

    except Exception as ex:

        instrument.status = "error"
        instrument.save(update_fields=["status"])

        messages.error(request, str(ex))

    return redirect("instrument_detail", pk=pk)

def instrument_list(request):

    search = request.GET.get("search", "")

    instruments = Instrument.objects.all()

    category = request.GET.get("category", "")

    status = request.GET.get("status", "")

    if search:
        instruments = instruments.filter(
            Q(name__icontains=search) |
            Q(manufacturer__icontains=search) |
            Q(model__icontains=search) |
            Q(serial_number__icontains=search) |
            Q(address__icontains=search)
        )

    if category:
        instruments = instruments.filter(category=category)

    if status:
        instruments = instruments.filter(status=status)

    context = {
        "instruments": instruments,
        "instrument_count": instruments.count(),
        "search": search,
        "category": category,
        "categories": InstrumentCategory.choices,
        "status": status,
        "statuses": InstrumentStatus.choices,
    }

    return render(request, "instruments/list.html", context)

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

        instrument.status = InstrumentStatus.ONLINE
        instrument.last_connected = timezone.now()
        instrument.save()

        messages.success(
            request,
            f"{instrument.name} connected"
        )

    except Exception as e:

        instrument.status = InstrumentStatus.ERROR
        instrument.save()

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

        driver.connect()

        identification = driver.identify()

        instrument.last_identification = identification
        instrument.save()

        messages.info(
            request,
            identification
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

def instrument_identify(request, pk):

    instrument = get_object_or_404(Instrument, pk=pk)

    try:
        identity = ConnectionService.identify(instrument)

        messages.success(
            request,
            f"Instrument identified: {identity}"
        )

    except Exception as ex:

        messages.error(request, str(ex))

    return redirect("instrument_detail", pk=pk)

def instrument_identify(request, pk):

    instrument = get_object_or_404(Instrument, pk=pk)

    try:

        identity = InstrumentService.identify(instrument)

        messages.success(
            request,
            f"Identification successful: {identity}"
        )

    except Exception as ex:

        messages.error(request, str(ex))

    return redirect("instrument_detail", pk=pk)