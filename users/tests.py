from audioop import reverse
import unittest
from django.test import TestCase, Client

# Create your tests here.


class IndexTests(unittest.TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_status_code(self):
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)

    def test_none_status_code(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
