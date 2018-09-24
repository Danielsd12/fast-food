from flask import Flask
from flask_restful import Api, Resource,request 

app = Flask(__name__)
api = Api(app)
METHODS=['GET'],['POST'],['PUT']



ORDERS =  {
    'order1': {'pizza': 700000},
    'order2': {'Sausage': 35000},
    'order3': {'Roasted_meat': 50000},
}

##app.route('/api/v1.0/new_order', methods=['POST']) 
##@app.route('/api/v1.0/get_order', method=['GET'])


#####          get orders    ########

class order(Resource):
    def get(self):
        return {
        "order": "all orders",
        "client":
        {
        "first_name": "Sserunkuma",
        "last_name": "Daniel",
        },


   "requested_items":
   {
       "order_id": "001",
       "food_items": ["chipse","Sausage","Roasted_meat"],
       "chipse_price": 10000,
       "Sausage_price": 24000,
       "Roasted_meat_price": 30000,
   },


   "residence": 
   {
         "city": "Nakawa",
         "country": "Uganda",
      }
        }

    def get_order_id(self):
        return {
        "order": "all orders",
        "client":
        {
        "first_name": "Sserunkuma",
        "last_name": "Daniel",
        },


   "requested_items":
   {
       "order_id": "001",
       "food_items": ["chipse","Sausage","Roasted_meat"],
       "chipse_price": 10000,
       "Sausage_price": 24000,
       "Roasted_meat_price": 30000,
   },


   "residence": 
   {
         "city": "Nakawa",
         "country": "Uganda",
        
      }
        }




    #def get_order_id(self,order_id):
     #   return
    #order_by_id = {
      #      "order_id":"001",
      #      "order_id":"002",
      #      "order_id":"003", 
       #      }







  
##@app.route('/api/v1.0/order', methods=['PUT'])
##class order_id(Resource):

###############        put endpoint      ###############
    def put(self):
        return {
        "order": "all orders",
        "client":
        {
        "first_name": "Namatovu",
        "last_name": "Milly",
        },


   "requested_items":
   {
       "order_id": "002",
       "food_items": ["pizza","golilos","chicken"],
       "pizza_price": 21000,
       "golilos_price": 45000,
       "chicken_price": 50000,
   }

    }

   #######         my post end point method   #   ## # #####  
##@app.route('/api/v1.0/new_order', methods=['POST'])   
##class new_order(Resource):

    def post(self):
        return {
        "order": "all orders",
        "client":
        {
        "first_name": "Namanda",
        "last_name": "Betty",
        },


   "requested_items":
   {
       "order_id": "003",
       "food_items": "chicken",
       "price": 40000,
   },


   "residence": 
   {
         "city": "Kasubi",
         "country": "Uganda",
      }

    }    


##@app.route('/api/v2.0/order', methods=['POST'])
##def post(self , order_id):
  ##  return {order_id: order[order_id]} 



##@app.route('/api/v3.0/order', methods=['PUT'])
##def put(self, order_id):      
 ##   return {order_id: order[order_id]} 
    
 
##class new_order(Resource):
   ## def get(self):
    ##    return {'order': 'new_orders'}


##class order_id(Resource):
  ##  def post(self,order_id):
     ##   return {order_id: order[order_id]}    

##api.add_resource(new_order,'/order_id')
api.add_resource(order, '/')
##api.add_resource(order, '/')
##api.put_resource(order, '/')
##api.add_resource(order, '/order/<order_id>')


if __name__ == '__main__':
    app.run(debug=True)