import uuid 
from flask import Flask, request
from flask_smorest import abort 
from db import items, stores

app2 = Flask(__name__)

@app2.get("/store")
def get_stores():
    return {"stores": list(stores.values())}

@app2.get("/store/<string:store_id>") #/store is the endpoint #GET - READ STORE
def get_store(store_id): #won't return information about items
    try:
        return stores[store_id] #accesses the specific store with 
        #that id in our dictionary and returns that dictionary of data
    except KeyError:
        abort(404, message="Store not found.")

@app2.post("/store") #this is 127:0.0.1/5000/store - creating an empty items list and adding to above stores list
def create_store(): # POST - CREATE STORE
    store_data = request.get_json()
    if "name" not in store_data: #must make sure that name is inside of the insomnia request as a key
        abort(
        400,
        message="ensure name is included in the insomnia request." 
        
    )
    for store in stores.values(): #if store is already in the stores dictionary, it would be a duplicate
        if store["name"] in stores:
            abort(400, message=f"store already exists")


    store_id = uuid.uuid4().hex #creates the item id
#    #unpacks values in store_data dictionary in the request and includes in new dictionary 
    
    store = {**store_data, "id": store_id} #passing keyword arguments to constructor
#    #id is a seperate key within this dictionary 
    stores[store_id] = store
    return store, 201 #200 is the default status code for ok while 201 means we have accepted the data into our store

@app2.delete("/store/<string:store_id>")
def delete_store(store_id):
    try:
        del stores[store_id]
        return {"message": "Store deleted."}
    except KeyError:
        abort(404, message="Store not found. ")



@app2.post("/item") #rename endpoint because we are not creating items in a store
def create_item(): 
    item_data = request.get_json()
    if (
        "price" not in item_data #we are making sure that either price, store_id, or name must
        #be included as a key in the insomnia request to be able to search in the item_data dictionary
        or "store_id" not in item_data
        or "name" not in item_data
    ):    #we are adding error handling to make the message more meaningful
        abort (
            400,
            message="Bad request. Ensure 'price' 'store_id', and 'name' are incuded in the json payload."
        )
    for item in items.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message=f"Item already exists.")
    if item_data["store_id"] not in stores: #checks dictionary to make sure store_id matches the request
        abort(404, message="Store not found.")
       
    item_id = uuid.uuid4().hex #creates item_id
    item = {**item_data, "id": item_id} #saves item_id to dictionary
    items[item_id] = item #places the item into our items dictionary
    return item, 201



@app2.get("/item/<string:item_id>") #getting item_id in the url
def get_item(item_id): #we are getting item from the items dictionary
    #maybe we need a request.get_json()?
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found.")


@app2.delete("/item/<string:item_id>") #issue
def delete_item(item_id): 
    try:
        del items[item_id]
        return {"message": "Item deleted."}
    except KeyError:
        abort(404, message="Item not found.")

@app2.put("/item/<string:item_id>") 
def update_item(item_id): #problem point
    item_data = request.get_json() #input value
    if "price" not in item_data or "name" not in item_data: #we require name and price as keys in the put request
        abort(400, message="must include name and price keys in insomnia request")
    
    try:
        item = items[item_id] #items dictionary + item_data key = value 
        item |= item_data #merging dictionaries - item_data dictinonary replaces item dictionary
        
        return item 
    except KeyError:
        abort(404, message="Item not found")

@app2.get("/item")
def get_all_items():
    return {"Hello World"}
    return {"items": list(items.values())} # we can now directly call the items dictionary's
    #keys to get the values instead of having to iterate over the list to get the store
