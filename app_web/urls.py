from django.contrib import admin
from django.urls import path, include


from location import urls as location_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(location_urls)),
]

