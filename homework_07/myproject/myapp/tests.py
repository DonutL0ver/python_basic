
from django.test import TestCase
from django.urls import reverse
from .models import Product

class MyModelTests(TestCase):

    def setUp(self):
        self.my_model_1 = Product.objects.create(name='Test Name 1', description='Test Description 1', price=10.99)
        self.my_model_2 = Product.objects.create(name='Test Name 2', description='Test Description 2', price=20.99)

    def tearDown(self):
        Product.objects.all().delete()

    def test_my_view_context(self):
        response = self.client.get(reverse('product_list'))

        self.assertEqual(response.status_code, 200)


        self.assertIn('products', response.context)
        my_model_list = response.context['products']
        self.assertEqual(list(my_model_list), [self.my_model_1, self.my_model_2])


        print('Response content:', response.content)
        print('Product list:', my_model_list)


        self.assertContains(response, 'Test Name 1')
        self.assertContains(response, 'Test Name 2')
