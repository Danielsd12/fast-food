# fast-food

this is an online restaurant, food delievary application.It is designed with front end User Interfaces(UIs) 
to anable consistent access,interactive access between clients and the application.
https://danielsd12.github.io/fast-food/home.html

THE FUNCTIONALITIES OF THE  APPLICATION.
fast-food application is embedded into different modules.
i) The user creates an account though signup module
ii) The user can therefore sign into the system after creating an account.
iii) The user makes an order according to the food items of their choice.
iii) The user can alter the order if he or she ordered incorrect food items.

SIGN UP
The sign up module will allow and manage all customers and other application users
to get accounts in the application.

SIGN IN
This module will capture client information they used when creating accounts. The signup
will be authenticated with customer mobile number and the password. 


THE APPLICATION PROGRAMING INTERFACE (API)
The is the middle tire of the fast-food application.It is normaly used for 
testing the end point and the routes.
This is done through using postman.
The (api) is embedded with the POST , PUT and GET methods.The methods are used 
to test the client and the administrator interaction with the application when making orders.
https://github.com/danielsd12/fast-food/tree/api/api


ACCESS TO THE APPLICTION

Use the web browsers Chrome or mozira firefox.
Install the virtual environment 
Install python 3.6.5
Get access to to python and install it here https://realpython.com/installing-python/


APPLICATION FEATURES
Client signup as new to the application
Client login if account exists.
client makes orders
client retrives and modify the order
Administrator adds am order,deletes an order

END POINTS

HTTP Method 	End point 	Action
POST 	/api/v1/orders 	Place an order
GET 	/api/v1/orders 	Get all orders
GET 	/api/v1/orders/ 	Fetch a specific order
PUT 	/api/v1/orders/ 	Update the status of an order


DESSIGNED WITH

css
python
html

Authors

Sserunkuma Daniel






