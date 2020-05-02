import unittest

# 11-1
print("\n11-1")
from city_country import city_countrys
class test_city(unittest.TestCase):
    def test_city_country(self):
        result = city_countrys("beijing", "china")
        self.assertEqual(result, "Beijing, China")

# 11-2
print("\n11-2")
from city_country import  city_country_population
class test_city2(unittest.TestCase):
    def test_city_country_population_1(self):
        result = city_country_population("beijing", "china")
        self.assertEqual(result, "Beijing, China - population 100")

    def test_city_country_population_2(self):
        result = city_country_population("beijing", "china", 500)
        self.assertEqual(result, "Beijing, China - population 500")

# 11-3
print("\n11-3")
from Employee import  Employees
class test_employee(unittest.TestCase):
    def setUp(self):
        self.worker = Employees("Ben", "Jack", 10000)

    def test_give_raise_1(self):
        self.worker.give_raise(3000)
        self.assertEqual(self.worker.salary, 13000)