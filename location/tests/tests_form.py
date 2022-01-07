from django.test import TestCase
from ..forms import CustomerForm


class LocationFormTests(TestCase):
    def test_location_form(self):
        name = 'patos'
        latitude = '-7.1057018'
        longitude = '-34.8441424'
        time = '2021-02-10'
    
        form_data = {
            'name': name, 
            'latitude': latitude, 
            'longitude': longitude,
            'time': time
        }
        form = CustomerForm(data=form_data)    
        self.assertTrue(form.is_valid())

