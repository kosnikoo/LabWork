import unittest
from src.MyProject import Triangle

class TestMyProject(unittest.TestCase):

    def test_valid_equilateral(self):
        status, vertices = Triangle(5, 5, 5)
        self.assertEqual(status, "Равносторонний")
        self.assertEqual(vertices[0], (0, 0))

    def test_valid_isosceles_ab(self):
        status, _ = Triangle(5, 5, 3)
        self.assertEqual(status, "Равнобедренный")

    def test_valid_isosceles_ac(self):
        status, _ = Triangle(5, 3, 5)
        self.assertEqual(status, "Равнобедренный")

    def test_valid_isosceles_bc(self):
        status, _ = Triangle(3, 5, 5)
        self.assertEqual(status, "Равнобедренный")

    def test_valid_scalene(self):
        status, vertices = Triangle(3, 4, 5)
        self.assertEqual(status, "Разносторонний")

    def test_valid_float_sides(self):
        status, _ = Triangle(3.5, 4.5, 5.5)
        self.assertEqual(status, "Разносторонний")

    def test_valid_large_numbers(self):
        status, _ = Triangle(10000, 10000, 10000)
        self.assertEqual(status, "Равносторонний")

    def test_valid_small_numbers(self):
        status, _ = Triangle(0.01, 0.01, 0.01)
        self.assertEqual(status, "Равносторонний")

    def test_invalid_sum_ab_equals_c(self):
        status, vertices = Triangle(2, 3, 5)
        self.assertEqual(status, "Не треугольник")
        self.assertEqual(vertices[0], (-1, -1))

    def test_invalid_sum_ac_equals_b(self):
        status, _ = Triangle(2, 5, 3)
        self.assertEqual(status, "Не треугольник")

    def test_invalid_sum_bc_equals_a(self):
        status, _ = Triangle(5, 2, 3)
        self.assertEqual(status, "Не треугольник")

    def test_invalid_sum_ab_less_than_c(self):
        status, _ = Triangle(2, 2, 10)
        self.assertEqual(status, "Не треугольник")

    def test_invalid_sum_ac_less_than_b(self):
        status, _ = Triangle(2, 10, 2)
        self.assertEqual(status, "Не треугольник")

    def test_invalid_sum_bc_less_than_a(self):
        status, _ = Triangle(10, 2, 2)
        self.assertEqual(status, "Не треугольник")

    def test_zero_side_a(self):
        status, _ = Triangle(0, 4, 5)
        self.assertEqual(status, "Не треугольник")

    def test_zero_side_b(self):
        status, _ = Triangle(3, 0, 5)
        self.assertEqual(status, "Не треугольник")

    def test_zero_side_c(self):
        status, _ = Triangle(3, 4, 0)
        self.assertEqual(status, "Не треугольник")

    def test_negative_side_a(self):
        status, _ = Triangle(-3, 4, 5)
        self.assertEqual(status, "Не треугольник")

    def test_negative_side_b(self):
        status, _ = Triangle(3, -4, 5)
        self.assertEqual(status, "Не треугольник")

    def test_type_string_input(self):
        status, vertices = Triangle("a", 4, 5)
        self.assertEqual(status, "Некорректные данные")
        self.assertEqual(vertices[0], (-2, -2))

    def test_type_all_strings_input(self):
        status, _ = Triangle("dwasada", "wdas", "wadc")
        self.assertEqual(status, "Некорректные данные")

if __name__ == '__main__':
    unittest.main()