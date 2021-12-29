from django.test import TestCase
from rest_framework.test import APIClient

from app.category.models import Category


class CategoryTest(TestCase):
    """
        Test categories endpoint for 5 functions
    """

    def create_category(self, name='Food'):
        category = Category(name=name)
        category.save()
        return category.id

    def get_category(self, id):
        return Category.objects.filter(id=id).first()

    def setUp(self):
        self.client = APIClient()

    def test_create_function(self):

        category_data = {"name": "Pasta"}

        response = self.client.post('/categories/', category_data)
        total_category = Category.objects.count()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, total_category)

    def test_list_function(self):
        self.create_category()

        response = self.client.get('/categories')
        categories = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(categories))
        self.assertEqual('Food', categories[0]['name'])

    def test_retrieve_function(self):
        id = self.create_category(name='Pizza')
        self.create_category(name='Chinese Food')

        response = self.client.get('/categories/{id}/'.format(id=id))
        categories = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Pizza', categories['name'])

    def test_update_function(self):
        id = self.create_category(name='Dessert')

        body = {'name': 'new category'}
        response = self.client.patch('/categories/{id}/'.format(id=id), data=body)

        category = self.get_category(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('new category', category.name)

    def test_delete_function(self):
        id = self.create_category()

        response = self.client.delete('/categories/{id}/'.format(id=id))

        category = self.get_category(id)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(category)

