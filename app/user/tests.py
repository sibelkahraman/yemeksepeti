from django.test import TestCase
from rest_framework.test import APIClient

from app.user.models import User


class CategoryTest(TestCase):
    """
        Test users endpoint for 5 functions
    """

    def create_user(self, phone, email):
        user = User(name='test',
                    surname='test',
                    phone=phone,
                    email=email)
        user.save()
        return user.id

    def get_user(self, id):
        return User.objects.filter(id=id).first()

    def setUp(self):
        self.client = APIClient()

    def test_create_function(self):

        user_data = {"name": "test",
                     "surname": "test",
                     "phone": "05550000000",
                     "email": "test@gmail.com"}

        response = self.client.post('/users/', user_data)
        total_user = User.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, total_user)

    def test_list_function(self):
        self.create_user(phone='05552223344', email='email@gmail.com')

        response = self.client.get('/users')
        users = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(users))
        self.assertEqual('05552223344', users[0]['phone'])

    def test_retrieve_function(self):
        id = self.create_user(phone='05009998877', email='test1@gmail.com')
        self.create_user(phone='05556667799', email='test2@gmail.com')

        response = self.client.get('/users/{id}/'.format(id=id))
        user = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual('05009998877', user['phone'])

    def test_update_function(self):
        id = self.create_user(phone='05002223344', email='test@gmail.com')

        body = {'name': 'new user'}
        response = self.client.patch('/users/{id}/'.format(id=id), data=body)

        user = self.get_user(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('new user', user.name)

    def test_delete_function(self):
        id = self.create_user(phone='05001112233', email='t@gmail.com')

        response = self.client.delete('/users/{id}/'.format(id=id))

        user = self.get_user(id)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(user)

