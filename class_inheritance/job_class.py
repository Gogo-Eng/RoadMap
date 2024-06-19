#!/usr/bin/python3

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last,  pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@gmail.com"

    def fullname(self):
        return(f"{self.first} {self.last}")
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.pgl = programming_language

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)  
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employees(self, emp):
        if emp not in self.employees:  
            self.employees.append(emp)

    def remove_employees(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employeees(self):
        for emp in self.employees:
            print(emp.fullname())







object_1 = Developer("Progress", "Gogo", 250000, "Python")
object_2 = Employee("Wisdom", "Gogo", 100000)
print(object_1.fullname())
print(object_2.fullname())
manager_1 = Manager("Anointing", "Gogo", 1000000)
print("Manager email: ", manager_1.email)
manager_1.add_employees(object_1)
manager_1.add_employees(object_2)
manager_1.remove_employees(object_1)
manager_1.print_employeees()
print(issubclass(Manager, Employee))