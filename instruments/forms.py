from django import forms
from .models import Instrument


class InstrumentForm(forms.ModelForm):

    class Meta:
        model = Instrument
        fields = [
            "name",
            "manufacturer",
            "model",
            "serial_number",
            "category",
            "interface",
            "address",
            "location",
            "status",
            "description",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }