
from django.test import TestCase, Client
from capitals.views import *

# Create your tests here.

class CapitalsTest(TestCase):

	def setUp(self):
	
		self.c=Client()
		
	def test_badnameofcapital(self):
		
		resp = self.c.post("/search/", {"country_capital": "dasdasdas"})
        	self.assertEquals(resp.status_code, 404)
        	
        def test_ok(self):
        	resp = self.c.post("/search/", {"country_capital": "MADRID"})
        	self.assertEquals(resp.status_code, 200)
