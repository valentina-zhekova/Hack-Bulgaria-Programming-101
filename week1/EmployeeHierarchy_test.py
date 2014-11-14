import unittest
from EmployeeHierarchy import *


class EmployeeHierarchyTests(unittest.TestCase):

    def setUp(self):
        self.hourly_employee = HourlyEmployee("Morgan, Harry", 30.0)
        self.salaried_employee = SalariedEmployee("Lin, Sally", 52000.0)
        self.manager = Manager("Smith, Mary", 104000.0, 50.0)

    def test_employee_init(self):
        self.employee = Employee("Mark")
        self.assertEqual("Mark", self.employee.name)

    def test_employee_get_name(self):
        self.employee = Employee("Mark")
        self.assertEqual("Mark", self.employee.getName())

    def test_hourly_employee_init(self):
        self.assertEqual(30.0, self.hourly_employee.hourly_wage)

    def test_hourly_employee_weeklyPay_less_than_40_hours(self):
        self.assertEqual(120.0, self.hourly_employee.weeklyPay(4))

    def test_hourly_employee_weeklyPay_more_than_40_hours(self):
        self.assertEqual(1290.0, self.hourly_employee.weeklyPay(42))

    def test_salaried_employee_init(self):
        self.assertEqual(52000.0, self.salaried_employee.annual_salary)

    def test_salaried_employee_weeklyPay(self):
        self.assertEqual(52000.0, self.salaried_employee.weeklyPay(42))

    def test_manager_init(self):
        self.assertEqual(50.0, self.manager.weekly_bonus)

    def test_manager_weeklyPay(self):
        self.assertEqual(104050.0, self.manager.weeklyPay(42))

    def test_employee_hierarchy(self):
        staff = []
        staff.append(self.hourly_employee)
        staff.append(self.salaried_employee)
        staff.append(self.manager)
        print('\n')
        for employee in staff:
            hours = int(input("Hours worked by " + employee.getName() + ": "))
            pay = employee.weeklyPay(hours)
            print("Salary: %.2f" % pay)

if __name__ == '__main__':
    unittest.main()
