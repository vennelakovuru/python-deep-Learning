class Employee:
    # class variables
    count = 0
    totalsal = 0

    # constructor initializing name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count += 1
        Employee.totalsal += self.salary

    # method to calculate average salary
    def avgsal(self):
        avgsal = Employee.totalsal / Employee.count
        return avgsal


# FullTimeEmployee Class inheriting the parent class Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department, etype):
        Employee.__init__(self, name, family, salary, department)
        self.etype = etype


# Instance creation of parent class Employee
Employee1 = Employee('Alish', 'Green', 90000, 'CS')
Employee2 = Employee('Jack', 'Sally', 66000, 'IT')
Employee3 = Employee('John', 'Doe', 33000, 'MECH')

# Instance creation of child class FullTimeEmployee
FullTimeEmployee1 = FullTimeEmployee('Rachel', 'Green', 30000, 'Cafe', 'fulltime')
FullTimeEmployee2 = FullTimeEmployee('Ross', 'Geller', 50000, 'Dino', 'fulltime')

print("Total number of employees::", Employee.count)
print("Average Salary of Employees::", FullTimeEmployee2.avgsal())
