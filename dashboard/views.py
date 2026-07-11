from django.shortcuts import render

from instruments.models import Instrument
from measurements.models import Measurement

def dashboard(request):

    instrument_count = Instrument.objects.count()

    online_count = Instrument.objects.filter(
        status="online"
    ).count()

    measurement_count = Measurement.objects.count()

    context = {
        "instrument_count": instrument_count,
        "online_count": online_count,
        "measurement_count": measurement_count,
        "project_count": 0,
        "alert_count": 0,
    }

    return render(
        request,
        "dashboard/index.html",
        context,
    )