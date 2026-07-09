from django.shortcuts import render
from instruments.models import Instrument

# Create your views here.
def index(request):
    return render(request, "dashboard/index.html")

def index(request):

    context = {
        "instrument_count": Instrument.objects.count(),
        "online_count": Instrument.objects.filter(status="online").count(),
        "offline_count": Instrument.objects.filter(status="offline").count(),
        "busy_count": Instrument.objects.filter(status="busy").count(),
    }

    return render(request, "dashboard/index.html", context)