import unittest
import datetime
from src.Delivery import calculate_delivery_cost

class TestDelivery(unittest.TestCase):

    def test_valid_normal_delivery(self):
        cost, date = calculate_delivery_cost(weight=1.0, distance=1000, package_type="обычный")
        self.assertEqual(cost, 5200)
        self.assertEqual(date, "2026-09-05")

    def test_weight_boundaries_min(self):
        self.assertEqual(calculate_delivery_cost(0.09, 1000, "обычный"), (-1, "0000-00-00"))

    def test_weight_boundaries_max(self):
        self.assertEqual(calculate_delivery_cost(50.1, 1000, "обычный"), (-1, "0000-00-00"))

    def test_distance_boundaries_min(self):
        self.assertEqual(calculate_delivery_cost(10.0, 0, "обычный"), (-1, "0000-00-00"))

    def test_distance_boundaries_max(self):
        self.assertEqual(calculate_delivery_cost(10.0, 5001, "обычный"), (-1, "0000-00-00"))

    def test_invalid_package_type(self):
        self.assertEqual(calculate_delivery_cost(10.0, 1000, "неизвестный"), (-1, "0000-00-00"))

    def test_weight_medium_multiplier(self):
        cost, _ = calculate_delivery_cost(10.0, 100, "обычный")
        self.assertEqual(cost, 840)

    def test_weight_heavy_multiplier(self):
        cost, _ = calculate_delivery_cost(20.0, 100, "обычный")
        self.assertEqual(cost, 1050)

    def test_package_type_fragile_surcharge(self):
        cost, _ = calculate_delivery_cost(1.0, 100, "хрупкий")
        self.assertEqual(cost, 1000)

    def test_package_type_dangerous_surcharge(self):
        cost, _ = calculate_delivery_cost(1.0, 100, "опасный")
        self.assertEqual(cost, 1700)

    def test_express_delivery_cost(self):
        standard_cost, _ = calculate_delivery_cost(1.0, 1000, "обычный", is_express=False)
        express_cost, _ = calculate_delivery_cost(1.0, 1000, "обычный", is_express=True)
        self.assertTrue(express_cost > standard_cost, "Экспресс-доставка должна стоить больше стандартной")

    def test_express_delivery_time_short_distance(self):
        _, date = calculate_delivery_cost(1.0, 100, "обычный", is_express=True)
        self.assertNotEqual(date, "2026-09-03", "Доставка не должна занимать 0 дней даже в экспресс-режиме")

if __name__ == '__main__':
    unittest.main()