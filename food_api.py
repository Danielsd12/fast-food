from flask import Flask, request, jsonify, json
app = Flask(__name__)


orders = [{'order': 1, 'Sserunkuma': 'Daniel'},
           {'order':2, 'Nabakka': 'Betty'},
           {'order':3, 'Emma': 'Mawanda'},]
           
           
@app.route('/api/v1/orders', methods=('GET', 'POST','PUT'))     

def order(self):

    if request.method == 'GET':
        response = orders
    else:  
        if request.content_type != 'application/json':
            return jsonify({})
        try:
            new_orders = json.loads(request.data)
           ## except ValueError:
            return jsonify({})
            if 'order' in new_orders and isinstance(new_orders['order'], int) and \
            'order' in new_orders and isinstance(new_orders['order'], basestring) and \
             len(new_orders.keys()) == 2 and new_orders not in orders:
             orders.append(new_orders)
             response = orders[-1]
            else:
                 return jsonify({})
                 return jsonify(response)
 if __name__ == '__main__':
      app.run(debug=True)                