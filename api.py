from flask import Flask, request, jsonify, json
app = Flask(__name__)


''' i have created a list as a data structure that will help
 me save or hold my data that has been 
appended to the list and this will finally work as my datastore.'''


orders = [{'orderid':1 , 'name': 'molly', 'residence':'kasubi',  'item':'chipse',   'price':'4500'}]
 
'''
implimenting a route , this route undertakes two methods. these include 
the POST method and the GET method.
  These will be my end points to or headers to run the get and post functionalities in my fast-food 
  application. 
  '''

@app.route('/api/v1/order', methods=('GET', 'POST'))
def order():
    if request.method == 'GET':
        response = orders

        #### POST ######
    else:  
        if request.content_type != 'application/json':
            return jsonify({}),200
        try:
            new_orders = json.loads(request.data)
        except ValueError:
            return jsonify({})

        print("before if")
        if 'orderid' in new_orders and isinstance(new_orders['orderid'], int) and \
           'name' in new_orders and isinstance(new_orders['name'], str) and \
           'residence' in new_orders and isinstance(new_orders['residence'],str) and\
           'item' in new_orders and isinstance(new_orders['item'],str) and\
         'price' in new_orders and isinstance(new_orders['price'],int) and\
           len(new_orders.keys()) == 5 and new_orders not in orders:
           print("after if")
           orders.append(new_orders)
           response = orders[-1]
        else:

            ###### am testing to see whether my code run upto here  #######

            return jsonify("The Validation Failed")
    return jsonify(response)


@app.route('/api/v1/order/<int:orderid>', methods=('PUT', 'DELETE'))

def update_orders(orderid):

    if request.method == 'DELETE':
        del orders [orderid]
        return jsonify(orderid)

    else: 
        orders[orderid] = json.loads(request.data)
        return jsonify({})
                
if __name__ == '__main__':
    app.run(debug=True)