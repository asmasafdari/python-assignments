class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    @staticmethod
    def from_fahrenheit(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def from_kelvin(kelvin):
        return kelvin - 273.15

if __name__ == "__main__":
    temp = TemperatureConverter(25)
    print("Celsius to Fahrenheit:", temp.to_fahrenheit())  # Output: 77.0
    print("Celsius to Kelvin:", temp.to_kelvin())          # Output: 298.15

    print("Fahrenheit to Celsius:", TemperatureConverter.from_fahrenheit(77))  # Output: 25.0
    print("Kelvin to Celsius:", TemperatureConverter.from_kelvin(298.15))      # Output: 25.0