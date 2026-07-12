from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)

from django.contrib import messages

from django.db.models import Q

from .models import (
    Instrument,
    InstrumentStatus,
    InstrumentCategory,
)

from .forms import InstrumentForm

from measurements.models import Measurement

from services.instrument_service import InstrumentService
from services.measurement_service import MeasurementService

def instrument_connect(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk,
    )

    try:

        InstrumentService.connect(instrument)

        messages.success(
            request,
            f"{instrument.name} connected successfully."
        )

    except Exception as ex:

        messages.error(
            request,
            str(ex),
        )

    return redirect(
        "instrument_detail",
        pk=pk,
    )

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
        pk=pk,
    )

    last_measurement = (
        Measurement.objects
        .filter(instrument=instrument)
        .order_by("-timestamp")
        .first()
    )

    recent_measurements = (
        Measurement.objects
        .filter(instrument=instrument)
        .order_by("-timestamp")[:10]
    )

    return render(
        request,
        "instruments/detail.html",
        {
            "instrument": instrument,
            "last_measurement": last_measurement,
            "recent_measurements": recent_measurements,
        },
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

def instrument_identify(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk,
    )

    try:

        identity = InstrumentService.identify(
            instrument
        )

        messages.success(
            request,
            identity,
        )

    except Exception as ex:

        messages.error(
            request,
            str(ex),
        )

    return redirect(
        "instrument_detail",
        pk=pk,
    )

def instrument_measure(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk,
    )

    try:

        measurement = MeasurementService.measure(
            instrument,
            "voltage",
        )

        messages.success(
            request,
            f"{measurement.value} {measurement.unit}",
        )

    except Exception as ex:

        messages.error(
            request,
            str(ex),
        )

    return redirect(
        "instrument_detail",
        pk=pk,
    )

def instrument_console(request, pk):

    instrument = get_object_or_404(
        Instrument,
        pk=pk,
    )

    response = ""

    if request.method == "POST":

        command = request.POST.get(
            "command",
            "",
        )

        try:

            driver = InstrumentService.connect(
                instrument
            )

            response = driver.query(
                command + "\n"
            )

        except Exception as ex:

            response = str(ex)

    return render(
        request,
        "instruments/console.html",
        {
            "instrument": instrument,
            "response": response,
        },
    )