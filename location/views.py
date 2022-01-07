from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.views.generic import (
    CreateView,
    UpdateView
)

from .models import Location
from .forms import CustomerForm

from geopy.distance import geodesic


def list_locations(request):
    locals = Location.objects.all()

    for lo in locals:
        lo.latitude = str(lo.latitude).replace(',', '.')
        lo.longitude = str(lo.longitude).replace(',', '.')

    context = {
        'locations': locals
    } 

    return render(request, 'home.html', context)


class LocationCreateView(CreateView):
    template_name = 'location/create_location.html'
    model = Location
    form_class = CustomerForm

    success_url = reverse_lazy('list_locations')


class LocationUpadateView(UpdateView):
    model = Location
    template_name = 'location/create_location.html'
    
    fields = [
        'name',
        'time',
        'latitude',
        'longitude'
    ]
    
    success_url = reverse_lazy('list_locations')


def search_locations(request):
    qs = Location.objects.all()

    latitude = request.GET.get("latitude").replace(',', '.')
    longitude = request.GET.get("longitude").replace(',', '.')
    radius = request.GET.get("radius")

    if latitude and longitude and radius:
        
        for value in (latitude, longitude, radius):
            print(value)
            try:
                float(value)
            except ValueError:
                return JsonResponse(
                    {
                        'error': 'latitude/longitude/radius should be numbers'
                    }, status=400
                )

        qs_fliter = []

        for lo in qs:
            dis = geodesic((latitude, longitude), (lo.latitude, lo.longitude)).km
            print(dis)

            if dis <= float(radius):
                lo.latitude = str(lo.latitude).replace(',', '.')
                lo.longitude = str(lo.longitude).replace(',', '.')
                qs_fliter.append(lo)


        context = {
            'locations': qs_fliter
        }

        return render(request, 'home.html', context)

