import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
blb = Blueprint("stores", __name__, description = "Operations on stores") 
@blb.route("/store/<string:store_id>") 
class Store(MethodView): 
    def get(self, store_id): 
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")
    def delete(self, store_id): 
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
