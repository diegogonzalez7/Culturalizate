from django.test import TestCase, Client
from countries.views import *
# Create your tests here.
class CountriesViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_detail_view_post(self):
        response = self.client.post('/detail/', {'country_name': 'Spain'})

        self.assertEqual(response.status_code, 200)

    def test_detail_view_invalid_post(self):
        response = self.client.post('/detail/', {'country_name': 'dadasdadasdas'})
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('countries:no_data'))


