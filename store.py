import uuid #generates unique identifiers
from flask import request #request object from Flask allows accessing info about current HTTP request
from flask.views import MethodView #MethodView is a class for defining class-based views in Flask
from flask_smorest import Blueprint, abort #Blueprint class and abort function from flask_smorest extension. Blueprint defines reusable and modular routes. abort returns error responses in restful api.
from db import stores #imports stores object from db module. seperate db.py file contains store data
blb = Blueprint("stores", __name__, description = "Operations on stores") #blb is instance of Blueprint class created with name "stores" and a description. Used to define routes for operations related to store.
@blb.route("/store/<string:store_id>") #decorator specifying route for Store class. store_id is dynamic paramater that can be any string. 
class Store(MethodView): #class based view named Store, which subclasses MethodView.
    def get(self, store_id): #get method - executed when http get is sent to route. retrieves store data from stores object using provided store_id. 
        try: #if store is found, return as response. 
            return stores[store_id]
        except KeyError: #if store is not found, aka keyerror, 404 error is raised using custom error message.
            abort(404, message="Store not found.")
    def delete(self, store_id): #delete method - HTTP Delete request made to specified route. 
        #attempts to delete store data from stores object using store_id. 
        try: #store deleted successfully as id was a match - returns message key
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError: #keyerror meaning store not found, so return 404 like above. 
            abort(404, message="Store not found.")
