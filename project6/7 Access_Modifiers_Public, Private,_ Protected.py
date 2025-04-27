class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

# Object creation
emp = Employee("Sana", 50000, "123-45-6789")

print(emp.name)       # Public variable
print(emp._salary)    # Protected variable (not recommended to access directly)
# print(emp.__ssn)    # Private variable (will raise AttributeError)
