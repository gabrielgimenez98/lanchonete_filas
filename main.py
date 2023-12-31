from fastapi import FastAPI
import json
from time import sleep
from inputs import Order
from services.redis import Redis
from services.tasks import prepare_order

app = FastAPI()

@app.get("/")
def read_root():
    
    return {"Hello": "World"}

@app.post("/make_order")
def make_order(request:Order):
    payload = json.loads(request.json())
    redis_service = Redis()
    response = redis_service.add_order(payload)
    order_id = response["id"]
    prepare_order.apply_async(args=(order_id,))

    return {"message":"Seu pedido foi realizado"}

@app.get("/check_orders")
def check_orders():
    redis_service = Redis()
    results = redis_service.get_all()
    return {"results":results}