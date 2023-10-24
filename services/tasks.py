from time import sleep
from celery import Celery
from services.redis import Redis

app = Celery(
    broker='pyamqp://guest@localhost/'
)


@app.task
def prepare_order(order_id:int):
    redis_service = Redis()
    order = redis_service.get_order(order_id)
    order["status"] = "em andamento"
    redis_service.update_order(order_id=order_id, order=order)
    sleep(10)
    order["status"] = "pronto"
    redis_service.update_order(order_id=order_id, order=order)
    deliver_order.apply_async(args=(order_id,))
    return "Pedido pronto para entrega"

@app.task
def deliver_order(order_id:int):
    redis_service = Redis()
    order = redis_service.get_order(order_id)
    order["status"] = "em rota de entrega"
    redis_service.update_order(order_id=order_id, order=order)
    sleep(10)
    order["status"] = "entregue"
    redis_service.update_order(order_id=order_id, order=order)
    return "Pedido entregue"
