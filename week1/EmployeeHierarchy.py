class Employee:

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class HourlyEmployee(Employee):

    def __init__(self, name, hourly_wage):
        super().__init__(name)
        self.hourly_wage = hourly_wage

    def weeklyPay(self, hours):
        result = self.hourly_wage * hours
        if hours > 40:
            result += 0.5 * self.hourly_wage * (hours - 40)
        return result


class SalariedEmployee(Employee):

    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def weeklyPay(self, hours):
        return self.annual_salary


class Manager(SalariedEmployee):

    def __init__(self, name, annual_salary, weekly_bonus):
        super().__init__(name, annual_salary)
        self.weekly_bonus = weekly_bonus

    def weeklyPay(self, hours):
        return self.annual_salary + self.weekly_bonus
