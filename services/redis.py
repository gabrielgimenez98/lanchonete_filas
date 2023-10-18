import redis
import uuid


r = redis.Redis(host='localhost', port=6379, db=0)

class Redis():
    def add_order(self, order):
        random_uuid = str(uuid.uuid4())
        
        mounted_order = {
            "item": order["item"],
            "status": "pendente",
        }

        r.hmset(random_uuid, mounted_order)

        return self.get_order(random_uuid)

    def get_order(self, id):

        return r.hgetall(id)