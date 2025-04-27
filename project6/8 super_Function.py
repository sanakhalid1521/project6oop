class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calls the constructor of Person class
        self.subject = subject

# Object creation
teacher = Teacher("Mr. Sir Ali", "Information Technology")
print(f"Name: {teacher.name}, Subject: {teacher.subject}")
