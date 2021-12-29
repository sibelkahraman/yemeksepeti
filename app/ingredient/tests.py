from django.test import TestCase
from rest_framework.test import APIClient

from app.ingredient.models import Ingredient


class CategoryTest(TestCase):
    """
        Test ingredients endpoint for 5 functions
    """

    def create_ingredient(self, name='Meat'):
        ingredient = Ingredient.objects.create(name=name)
        return ingredient.id

    def get_ingredient(self, id):
        return Ingredient.objects.filter(id=id).first()

    def setUp(self):
        self.client = APIClient()

    def test_create_function(self):

        ingredient_data = {"name": "Egg"}

        response = self.client.post('/ingredients/', ingredient_data)
        total_ingredient = Ingredient.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, total_ingredient)

    def test_list_function(self):
        self.create_ingredient()

        response = self.client.get('/ingredients')
        ingredients = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(ingredients))
        self.assertEqual('Meat', ingredients[0]['name'])

    def test_retrieve_function(self):
        id = self.create_ingredient(name='Cheese')
        self.create_ingredient(name='Tomatoes')

        response = self.client.get('/ingredients/{id}/'.format(id=id))
        ingredients = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual('Cheese', ingredients['name'])

    def test_update_function(self):
        id = self.create_ingredient()

        body = {'name': 'new ingredient'}
        response = self.client.patch('/ingredients/{id}/'.format(id=id), data=body)

        ingredient = self.get_ingredient(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('new ingredient', ingredient.name)

    def test_delete_function(self):
        id = self.create_ingredient()

        response = self.client.delete('/ingredients/{id}/'.format(id=id))

        ingredient = self.get_ingredient(id)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(ingredient)

