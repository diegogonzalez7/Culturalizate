from django.test import TestCase, Client
from currencies.views import *

class CurrenciesViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_requests(self):
    
        response_search = self.client.post('/currencies/search/', {'country_currency': 'euro'})

        self.assertEqual(response_search.status_code, 200)
        self.assertTemplateUsed(response_search, 'currencies/currency.html')
        response_currency = self.client.post('/currencies/euro/')
 
        self.assertEqual(response_currency.status_code, 200)
    
