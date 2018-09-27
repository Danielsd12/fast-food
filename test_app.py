from api import app
import json
import unittest

class Test_Order(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)


    def test_get_orders(self):
        response = self.tester.get('/api/v1/order')
        self.assertEqual(response.status_code,200)

    ''' testing a single order '''
    def test_get_one_order(self):
        response = self.tester.get('/api/v1/order/1')
        self.assertEqual(response.status_code,200)    


    

        ##################################   end of my first test ####################


    def Test_Orderid(self,orderid):
        if orderid == str():
            return True
        elif orderid == int():
            return false

    class order_orderid(self,TestCase):
        if request.method == "DELETE":
            responce = self.tester.delete('/api/vi/orderid')     
        else:
            print("new order has been deleted")

########################   DELETE TEST     ####################
