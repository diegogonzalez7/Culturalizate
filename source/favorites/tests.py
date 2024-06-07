from django.test import TestCase, Client
from django.urls import reverse
from favorites.views import add_to_favorites, show_favorites

class FavoritesViewsTest(TestCase):

    def setUp(self):
        self.client = Client()


    def test_add_to_favorites_post_valid_country(self):
        response = self.client.post(reverse('favorites:add_to_favorites'), {'country_name': 'Spain'})
        self.assertRedirects(response, reverse('favorites:show_favorites'))#Comprobamos si redirige
        self.assertIn('favorites', self.client.session)
        self.assertIn('Spain', self.client.session['favorites'])#Verificamos si el pais esta en la lista

    def test_add_to_favorites_post_invalid_country(self):
        response = self.client.post(reverse('favorites:add_to_favorites'), {'country_name': 'sdadadasasd'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'countries/no_data.html')#Comprobamos que redirige a no_data

    def test_show_favorites_no_favorites(self):#Cuando todavía no hay favoritos
        response = self.client.get(reverse('favorites:show_favorites'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favorites/no_favorites.html')
