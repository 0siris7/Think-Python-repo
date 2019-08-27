import unittest
from employee import Employee 

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Aaron", "stone", 1200)
        self.salary = self.employee.salary

    def test_give_deafault_raise(self):
        self.employee.give_raise()
        self.assertNotEqual(self.salary, self.employee.salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(12000)
        self.assertNotEqual(self.salary, self.employee.salary)

unittest.main()
