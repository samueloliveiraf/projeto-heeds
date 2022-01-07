from django.test import TestCase, Client
from django.urls import reverse
from mixer.backend.django import mixer
from django.test import RequestFactory
import pytest

from location.models import Location

from ..views import (
    LocationUpadateView, 
    LocationCreateView
) 


class LocationViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('list_locations')
        self.create_url = 'create_location'


    def test_location_list_GET(self):
      
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    
    def test_location_upadate_GET(self):
        request = RequestFactory().get(self.list_url)
        object = mixer.blend('location.Location')
        response = LocationUpadateView.as_view()(request, pk=object.pk)
        assert response.status_code == 200, 'Sucess test update'

    
    def test_location_upadate_POST(self):
        object = mixer.blend('location.Location')
        data = {
            'name': 'joãopessoa',
            'latitude' :'-7.1057018',
            'longitude':'-34.8441424',
            'time':'2021-02-10 12:30:05'
        }
        request = RequestFactory().post(self.list_url, data=data)
        response = LocationUpadateView.as_view()(request, pk=object.pk)
        assert response.status_code == 302, 'Redirec view sucess'
        object.refresh_from_db()
        assert object.name == 'joãopessoa', 'Upadate location sucess'

    
    def test_location_create_POST(self):
        object = mixer.blend('location.Location')
        data = {
            'name': 'patos',
            'latitude' :'-7.1057018',
            'longitude':'-34.8441424',
            'time':'2021-02-10'
        }
        request = RequestFactory().post(self.create_url, data=data)
        response = LocationCreateView.as_view()(request)
        assert response.status_code == 302, 'Redirec view sucess'
        object.name = 'patos'
        assert object.name == 'patos', 'Create location sucess'

