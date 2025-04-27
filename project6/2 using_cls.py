class Counter:
    count = 0  # Class variable

    def __init__(self):
        Counter.count += 1  # Incrementing class variable for every new object

    @classmethod
    def display_count(cls):
        print(f"Objects created: {cls.count}")

# Creating objects
obj1 = Counter()
obj2 = Counter()

# Calling class method
Counter.display_count()  # This will output: Objects created: 2
