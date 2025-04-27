class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Static method call
temp = TemperatureConverter()
fahrenheit = temp.celsius_to_fahrenheit(30)
print(f"Temperature in Fahrenheit: {fahrenheit}")
