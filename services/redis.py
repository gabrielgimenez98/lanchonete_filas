import redis
import uuid


r = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)

class Redis():
    def add_order(self, order):
        random_uuid = int(uuid.uuid4())
        
        mounted_order = {
            "id": random_uuid,
            "item": order["item"],
            "status": "pendente",
        }

        r.hmset(random_uuid, mounted_order)

        return self.get_order(random_uuid)
    
    def update_order(self, order_id, order):
    
        r.hmset(order_id, order)

        return self.get_order(order_id)

    def get_order(self, id):

        return r.hgetall(id)
    
    def get_all(self):
        orders = []
        for key in r.keys():
            orders.append(self.get_order(id=int(key)))

        return orders