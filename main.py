from fastapi import FastAPI
import json
from time import sleep

from inputs import Order
from services.redis import Redis

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/make_order")
def make_order(request:Order):
    payload = json.loads(request.json())
    redis_service = Redis()
    response = redis_service.add_order(payload)
    return response

@app.post("/prepare_order/{order_id}")
def prepare_order(order_id:int):
    redis_service = Redis()
    order = redis_service.get_order(order_id)
    order["status"] = "em andamento"
    redis_service.update_order(order_id=order_id, order=order)
    sleep(10)
    order["status"] = "pronto"
    redis_service.update_order(order_id=order_id, order=order)

@app.post("/deliver_order/{order_id}")
def deliver_order(order_id:int):
    redis_service = Redis()
    order = redis_service.get_order(order_id)
    order["status"] = "em rota de entrega"
    redis_service.update_order(order_id=order_id, order=order)
    sleep(10)
    order["status"] = "entregue"
    redis_service.update_order(order_id=order_id, order=order)

@app.get("/check_orders")
def check_orders():
    redis_service = Redis()
    result = redis_service.get_all()
    return {"results":result}