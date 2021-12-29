from django.test import TestCase
from rest_framework.test import APIClient

from app.restaurant.models import Restaurant
from app.user.models import User
from app.food.models import Food
from app.order.models import Order


class CategoryTest(TestCase):
    """
        Test orders endpoint
    """

    def create_food(self, name):
        food = Food(name=name)
        food.save()
        return food

    def create_user(self, phone, email):
        user = User(name='test',
                    surname='test',
                    phone=phone,
                    email=email)
        user.save()
        return user

    def create_restaurant(self, phone, email):
        restaurant = Restaurant.objects.create(name='Rest',
                                               phone=phone,
                                               email=email)
        return restaurant

    def create_order(self):
        order = Order.objects.create(user=self.user,
                                     restaurant=self.restaurant)
        order.food.set([self.food])
        return order.id

    def create_order_by_endpoint(self):
        order_data = {"user": self.user.id,
                      "phone": "05550000000",
                      "restaurant": self.restaurant.id,
                      "food": [self.food.id]}

        response = self.client.post('/orders/', order_data)

        return response.data['id']

    def get_order(self, id):
        return Order.objects.filter(id=id).first()

    def setUp(self):
        self.client = APIClient()
        self.restaurant = self.create_restaurant(phone='05073332211',
                                                 email='restaurant@gmail.com')
        self.food = self.create_food(name='Food')
        self.user = self.create_user(phone='05073338899',
                                     email='user@gmail.com')

    def test_create_function(self):

        order_data = {"user": self.user.id,
                      "phone": "05550000000",
                      "restaurant": self.restaurant.id,
                      "food": [self.food.id]}

        response = self.client.post('/orders/', order_data)
        total_order = Order.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, total_order)

    def test_list_function(self):
        self.create_order()

        response = self.client.get('/orders')
        orders = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(orders))
        self.assertEqual("waiting", orders[0]['status'])

    def test_retrieve_function(self):
        id = self.create_order()
        self.create_order()

        response = self.client.get('/orders/{id}/'.format(id=id))
        self.assertEqual(response.status_code, 200)

    def test_update_order(self):
        id = self.create_order_by_endpoint()
        self.create_order_by_endpoint()

        total_order = Order.objects.filter(status='waiting').count()
        self.assertEqual(2, total_order)

        response = self.client.get('/orders/complete/')

        self.assertEqual(response.status_code, 200)

        released_order_number = Order.objects.filter(status='released').count()
        self.assertEqual(2, released_order_number)

        order = self.get_order(id)
        self.assertEqual('released', order.status)

    def test_delete_function(self):
        id = self.create_order()

        response = self.client.delete('/orders/{id}/'.format(id=id))

        order = self.get_order(id)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(order)

    def test_list_order_by_status_filter(self):
        self.create_order()

        response = self.client.get('/orders/waiting/')
        order = response.data[0]

        self.assertEqual(response.status_code, 200)
        self.assertEqual('waiting', order['status'])

