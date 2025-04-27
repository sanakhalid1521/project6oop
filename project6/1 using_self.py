class Student:
    def __init__(self, name, marks):
        self.name = name  # 'self' ka use karke instance variable assign kiya
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Sana", 95)  

s1.display()
