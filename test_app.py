from api import app
import json
import unittest

class Test_Order(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)


    def test_order(self):
        response = self.tester.get('/api/v1/order')
        self.assertEqual(response.status_code,200)
        