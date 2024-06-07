from django.test import TestCase, Client
from django.urls import reverse
from order.views import order_by_pop_asc, order_by_pop_desc, order_by_area_asc, order_by_area_desc

class OrderViewsTest(TestCase):

    def setUp(self):
        self.client = Client()


    def test_order_by_pop_desc(self):#Comprueba que el cabeza de lista sea china
        response = self.client.get(reverse('order:order_by_pop_desc'))
        self.assertEqual(response.status_code, 200)
        countries = response.context['data']
        populations = [country['population'] for country in countries]
        self.assertEqual(countries[0]['name']['common'], 'China')
        self.assertEqual(populations, sorted(populations, reverse=True))

    def test_order_by_area_asc(self):#Comprueba que el cabeza de lista sea ciudad del vaticano
        response = self.client.get(reverse('order:order_by_area_asc'))
        self.assertEqual(response.status_code, 200)
        countries = response.context['data']
        self.assertEqual(countries[0]['name']['common'], 'Vatican City')
        areas = [country['area'] for country in countries]
        self.assertEqual(areas, sorted(areas))


    def test_order_by_area_desc(self):#Comprueba que el cabeza de lista sea russia
        response = self.client.get(reverse('order:order_by_area_desc'))
        self.assertEqual(response.status_code, 200)
        countries = response.context['data']
        self.assertEqual(countries[0]['name']['common'], 'Russia')
        areas = [country['area'] for country in countries]
        self.assertEqual(areas, sorted(areas, reverse=True))
