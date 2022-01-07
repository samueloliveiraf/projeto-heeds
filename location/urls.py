from django.urls import path
from .views import (
    LocationCreateView,
    LocationUpadateView,
    search_locations,
    list_locations
)

urlpatterns = [
    path('', 
        list_locations,
        name='list_locations'
    ),
    path('create-location/', 
        LocationCreateView.as_view(),
        name='create_location'
    ),
    path('update-location/<int:pk>/',
        LocationUpadateView.as_view(),
        name='update_location'
    ),
    path('search-locations/', 
        search_locations,
        name='search_locations'
    )
]

