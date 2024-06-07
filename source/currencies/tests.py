from django.test import TestCase, Client
from currencies.views import *

class CurrenciesViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_requests(self):
    
        response_search = self.client.post('/search_currency/', {'country_currency': 'euro'})

        self.assertEqual(response_search.status_code, 200)
        self.assertTemplateUsed(response_search, 'currencies/b_currency.html')
        response_currency = self.client.post('/currency/EUR/')
 
        self.assertEqual(response_currency.status_code, 200)
     
      def test_post_requests_with_invalid_currency(self):
        
        response_search = self.client.post('/search_currency/', {'country_currency': 'XYZ'})
        self.assertEqual(response_search.status_code, 404)
        response_currency = self.client.post('/currency/XYZ/')
        self.assertEqual(response_currency.status_code, 404)
