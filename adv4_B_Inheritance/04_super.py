class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing...")

class Programmer(Employee):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary for programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so I am luckily breathing + +...")

print("\n")
p = Person()
p.takeBreath()
print("\n")

e = Employee()
e.takeBreath()
print("\n")

pr = Programmer()
pr.takeBreath()
print("\n")