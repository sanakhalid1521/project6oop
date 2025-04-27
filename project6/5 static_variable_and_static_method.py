class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b 

# Static method ko call karna
result = MathUtils.add(5, 3)  

print(f"The sum is: {result}")
