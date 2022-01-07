from django.test import TestCase

from ..models import Location


class LocationModelTestCase(TestCase):

    def setUp(self):
        Location.objects.create(
            name='joãopessoa',
            latitude='-7.1057018',
            longitude='-34.8441424',
            time='2021-02-10 12:30:05'
        )


    def test_create_new_location(self):
        lo = Location.objects.get(name='joãopessoa')
        self.assertEqual(lo.__str__(), 'joãopessoa')
