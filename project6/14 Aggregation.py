class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee  # Aggregation

# Object creation
emp = Employee("Sana")
dept = Department(emp)
print(f"Employee in department: {dept.employee.name}")
