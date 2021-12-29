import json

from django.test import TestCase
from rest_framework.test import APIClient
from model_mommy import mommy

from app.address.models import Address
from app.user.models import User


class AddressTest(TestCase):
    """
        Test addresses endpoint for 5 functions
    """

    def create_user(self):
        mommy.make(User)

    def create_address(self, city):
        user = User.objects.first()

        address = Address(country='C', city=city,
                          district='d', street='s',
                          building_number=0, user=user, type='h')
        address.save()
        return address.id

    def get_address(self, id):
        return Address.objects.filter(id=id).first()

    def setUp(self):
        self.client = APIClient()
        self.create_user()

    def test_create_function(self):
        user_id = User.objects.first().id

        address_data = {"country": "Country",
                        "city": "City",
                        "district": "District",
                        "street": "Street",
                        "building_number": 0,
                        "user": user_id,
                        "type": "h"}

        response = self.client.post('/addresses/', address_data)
        total_address = Address.objects.count()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, total_address)

    def test_list_function(self):
        self.create_address('')

        response = self.client.get('/addresses')
        addresses = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(addresses))
        self.assertEqual('h', addresses[0]['type'])

    def test_retrieve_function(self):
        id = self.create_address('city1')
        self.create_address('city2')

        response = self.client.get('/addresses/{id}/'.format(id=id))
        addresses = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual('city1', addresses['city'])

    def test_update_function(self):
        id = self.create_address('city1')

        body = {'city': 'new city'}
        response = self.client.patch('/addresses/{id}/'.format(id=id), data=body)

        address = self.get_address(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('new city', address.city)

    def test_delete_function(self):
        id = self.create_address('city1')

        response = self.client.delete('/addresses/{id}/'.format(id=id))

        address = self.get_address(id)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(address)

