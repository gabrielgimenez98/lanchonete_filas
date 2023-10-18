from fastapi import FastAPI
import json

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