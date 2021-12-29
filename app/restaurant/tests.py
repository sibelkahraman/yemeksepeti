from django.test import TestCase
from rest_framework.test import APIClient

from app.restaurant.models import Restaurant
from app.food.models import Food


class CategoryTest(TestCase):
    """
        Test restaurants endpoint for 5 functions
    """

    def create_restaurant(self, phone, email):

        restaurant = Restaurant.objects.create(name='Rest', phone=phone, email=email)
        return restaurant.id

    def get_restaurant(self, id):
        return Restaurant.objects.filter(id=id).first()

    def setUp(self):
        self.client = APIClient()

    def test_create_function(self):

        restaurant_data = {"name": "Lokanta",
                           "phone": "05550000000",
                           "email": "test@gmail.com"}

        response = self.client.post('/restaurants/', restaurant_data)
        total_restaurant = Restaurant.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, total_restaurant)

    def test_list_function(self):
        self.create_restaurant(phone='05552223344', email='email@gmail.com')

        response = self.client.get('/restaurants')
        restaurants = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(restaurants))
        self.assertEqual('05552223344', restaurants[0]['phone'])

    def test_retrieve_function(self):
        id = self.create_restaurant(phone='05009998877', email='test1@gmail.com')
        self.create_restaurant(phone='05556667799', email='test2@gmail.com')

        response = self.client.get('/restaurants/{id}/'.format(id=id))
        restaurant = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual('05009998877', restaurant['phone'])

    def test_update_function(self):
        id = self.create_restaurant(phone='05002223344', email='test@gmail.com')

        body = {'name': 'new restaurant'}
        response = self.client.patch('/restaurants/{id}/'.format(id=id), data=body)

        restaurant = self.get_restaurant(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('new restaurant', restaurant.name)

    def test_delete_function(self):
        id = self.create_restaurant(phone='05001112233', email='t@gmail.com')

        response = self.client.delete('/restaurants/{id}/'.format(id=id))

        restaurant = self.get_restaurant(id)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(restaurant)

