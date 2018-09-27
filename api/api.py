import json
from flask import request, jsonify
from datetime import date
from api import app

''' i have created a list as a data structure that will helpme save or hold my data that has been 
appended to the list and this will finally work as my datastore.'''

orders = []

'''this my order class that creates my order '''

class Order():

    '''this constructor is to initialise all the required attributes'''

    def __init__(self, orderid, name, item, price, residence):
        self.orderid = orderid
        self.name = name
        self.item = item
        self.residence = residence
        self.price = price

    '''this method changes my order class to a dictionary'''

    def change_to_json(self):
        return{
            "oderid":self.orderid,
            "name": self.name,
            "residence":self.residence,
            "item": self.item ,
            "price":self.price
        }

 
'''implimenting a route , this route undertakes two methods. these include 
the POST method and the GET method.  These will be my end points to run the get and post 
functionalities in my fast-food application.'''


@app.route('/api/v1/order', methods=['GET','POST'])
def add_order():
    if request.method == 'POST':
        input=request.get_json()
        orderid = len(orders) + 1
        name=input.get("name")
        residence=input.get("residence")
        item=input.get("item")
        price=input.get("price")

        new_order=Order(orderid ,name ,item ,residence ,price)
        orders.append(new_order)

        return jsonify({'order is:':new_order.change_to_json(), 'message': 'order added'}), 200
        
    else:
        
        # for order in orders:
        return orders 


@app.route('/api/v1/order/<int:orderid>', methods=['GET','PUT'])
def update_orders(orderid):

    if request.method == 'GET':
        for order in orders:
            if order["orderid"] == orderid:
                return jsonify({"order is:":order.change_to_json()})

    else: 
        for order in orders:
            if order["orderid"] == orderid:

                return jsonify({"order is:":order})
                



# len(new_orders.keys()) == 5 and new_orders not in orders

        # if 'name' in new_orders and isinstance(new_orders['name'], str) and \
        #    'residence' in new_orders and isinstance(new_orders['residence'],str) and\
        #    'item' in new_orders and isinstance(new_orders['item'],str) and\
        #    'price' in new_orders and isinstance(new_orders['price'],int) and\
        #    'orderid' in new_orders and isinstance(new_orders['orderid'],int) and\
        #    len(new_orders.keys()) == 5 and new_orders not in orders :
