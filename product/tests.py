from django.test import TestCase
from model_mommy import mommy 

# Create your tests here.

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = mommy.make('product.Category')

    def test_category_creation(self):
        """ Test Product Creation """
        self.assertEqual(self.category.__str__(), self.category.title) 


class ProductTestCase(TestCase):
    def setUp(self):
        self.product = mommy.make('product.Product')

    def test_product_creation(self):
        """ Test Product Creation """
        self.assertEqual(self.product.__str__(), self.product.title) 