from django.shortcuts import render

# Create your views here.
from .models import Measurement


def measurement_list(request):

    measurements = Measurement.objects.all()

    return render(
        request,
        "measurements/list.html",
        {
            "measurements": measurements
        }
    )