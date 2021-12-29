from django.test import TestCase
from rest_framework.test import APIClient

from app.food.models import Food
from app.category.models import Category
from app.ingredient.models import Ingredient


class CategoryTest(TestCase):
    """
        Test foods endpoint for 5 functions
    """

    def create_ingredient(self):
        ingredient = Ingredient.objects.create(name='Milk')
        return ingredient

    def create_category(self, name='Food'):
        category = Category.objects.create(name=name)
        return category

    def create_food(self, name='Soup'):

        food = Food.objects.create(name=name)
        food.category.set([self.category.id])
        food.ingredients.set([self.ingredient.id])
        food.save()

        return food.id

    def get_food(self, id):
        return Food.objects.filter(id=id).first()

    def setUp(self):
        self.client = APIClient()
        self.ingredient = self.create_ingredient()
        self.category = self.create_category()

    def test_create_function(self):

        food_data = {"name": "Pasta", "category": [self.category.pk], "ingredients": [self.ingredient.pk]}

        response = self.client.post('/foods/', food_data)
        total_food = Food.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(1, total_food)

    def test_list_function(self):
        self.create_food()

        response = self.client.get('/foods')
        foods = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(foods))
        self.assertEqual('Soup', foods[0]['name'])

    def test_retrieve_function(self):
        id = self.create_food(name='quattro formaggi')
        self.create_food(name='Dim Sum')

        response = self.client.get('/foods/{id}/'.format(id=id))
        foods = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEqual('quattro formaggi', foods['name'])

    def test_update_function(self):
        id = self.create_food()

        body = {'name': 'new food'}
        response = self.client.patch('/foods/{id}/'.format(id=id), data=body)

        food = self.get_food(id)
        self.assertEqual(response.status_code, 200)
        self.assertEqual('new food', food.name)

    def test_delete_function(self):
        id = self.create_food()

        response = self.client.delete('/foods/{id}/'.format(id=id))

        food = self.get_food(id)
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(food)

