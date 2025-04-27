class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Object creation
multiplier = Multiplier(5)
print(f"Result: {multiplier(3)}")  # Callable object
