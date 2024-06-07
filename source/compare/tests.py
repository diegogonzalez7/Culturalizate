from django.test import TestCase, Client
from django.urls import reverse
from compare.views import comp_countries

class CompareCountriesTest(TestCase):
	  def setUp(self):
        self.client = Client()

    def test_bad_country(self): # Intenta comparar un país que no existe
       
        response = self.client.get(reverse('compare:comp_countries', args=('Brazil', 'La Coru neno')))
        self.assertEqual(response.status_code, 404)

    def test_compare_countries(self): # Compara dos países válidos
       
        response = self.client.get(reverse('compare:comp_countries', args=('Brazil', 'Germany')))
        self.assertEqual(response.status_code, 200)
