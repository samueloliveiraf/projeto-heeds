from django import forms
from django.conf import settings

from .models import Location


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    name = forms.CharField(
        label='Nome'
    )
    time = forms.DateField(
        label='Data da viagem', 
        widget=DateInput(),
        input_formats=settings.DATE_INPUT_FORMATS
    )


    class Meta:
        model = Location
        fields = (
            'name',
            'time',
            'latitude', 
            'longitude'
        )

