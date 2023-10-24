from unittest import TestCase
from unittest.mock import Mock, patch
from inputs import Order
from main import make_order, check_orders

class TestTasks(TestCase):

    @patch("main.prepare_order")
    @patch("main.Redis")
    def test_make_order_success(self,mock_redis, mock_prepare_order):
        mock_redis.add_order().return_value = {"id":1, "status":"pendente","item":"nada"}
        order = Order(item="vegetariano")
        response = make_order(order)
        self.assertEqual(response,{"message":"Seu pedido foi realizado"})
        mock_redis.return_value.add_order.assert_called_with({"item": "vegetariano"})

    @patch("main.Redis")
    def test_check_order_success(self,mock_redis):
        expected_list = [{"id":1, "status":"pendente","item":"nada"}]
        redis_instance = mock_redis.return_value
        redis_instance.get_all.return_value = [{"id": 1, "status": "pendente", "item": "nada"}]
        response = check_orders()
        self.assertEqual(response,{"results":expected_list})
