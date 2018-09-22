from flask import Flask, request, jsonify, json

app = Flask(__name__)

orders = [{'orderid': 1, 'name': 'Sserunkuma Daniel','residence':'Lubaga',  'item':'chipse',   'price':23000},
           {'orderid': 2, 'name': 'Nagawa Ruth',     'residence':'mengo',     'item':'chicken','price':50000},
           {'orderid': 3, 'name': 'Namata Recheal',  'residence':'nakawa',   'item':'pizza',   'price':20000},
           {'orderid': 4, 'name': 'Sentanlo John',   'residence':'makindye',  'item':'coffe',   'price':5500},
           {'orderid': 5, 'name': 'John Bosco',      'residence':'kampala',   'item':'beaf',     'price':35000},
           {'orderid': 6, 'name': 'Omega Lutalo',    'residence':'namungoona',  'item': 'gollilos','price':12000},
           {'orderid': 7, 'name': 'Senyondo Robert', 'residence':'kamwokya',  'item':'hot dog',    'price':90000}]

@app.route('/api/v1/order', methods=('GET', 'POST'))
def order():
    if request.method == 'GET':
        response = orders
    else:  # POST
        if request.content_type != 'application/json':
            return jsonify({})
        try:
            new_orders = json.loads(request.data)
        except ValueError:
            return jsonify({})
            ########     code execeeds this level or reaches here
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
            ###### am testing to see whether my code run upto here  ######
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