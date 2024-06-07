from django.test import TestCase, Client
from django.urls import reverse
from languages.views import search_by_language, language

class LanguagesViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_search_by_language_post(self):
        response = self.client.post(reverse('languages:search'), {'country_language': 'Spanish'})
        self.assertRedirects(response, reverse('languages:language', kwargs={'language': 'Spanish'}))#Verifica que redirige a la vista donde el idioma es el esàñol

    def test_search_by_language_post_invalid_language(self):
        response = self.client.post(reverse('languages:search'), {'country_language': 'asddadsads'})
        self.assertEqual(response.status_code, 302)
