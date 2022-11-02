from django.test import TestCase
import random

from .models import Lawsuit

# Create your tests here.
class LawsuitTestCase(TestCase):
    def setUp(self):
        self.number_of_lawsuits = 10
        for i in range(self.number_of_lawsuits):
            Lawsuit.objects.create(number=f'{random.randint(154000, 1546000)}', description='a new lawsuit')

    def test_law_suit_creation(self):
        for lawsuit in Lawsuit.objects.all():
            print(lawsuit)