from unittest import TestCase
from unittest.mock import patch
from services.tasks import deliver_order, prepare_order

class TestTasks(TestCase):

    @patch("services.tasks.Redis")
    def test_deliver_order_success(self,mock_redis):
        mock_redis.get_order().return_value = {"id":1, "status":"pendente","item":"nada"}
        mock_redis.update_order().return_value = {"id":1, "status":"pendente","item":"nada"}
        response = deliver_order(1)
        self.assertEqual(response,"Pedido entregue")

    @patch("services.tasks.deliver_order")
    @patch("services.tasks.Redis")
    def test_prepare_order_success(self,mock_redis, mock_deliver_order):
        mock_redis.get_order().return_value = {"id":1, "status":"pendente","item":"nada"}
        mock_redis.update_order().return_value = {"id":1, "status":"pendente","item":"nada"}
        response = prepare_order(1)
        self.assertEqual(response,"Pedido pronto para entrega")