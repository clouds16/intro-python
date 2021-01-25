import enum


class TemperatureUnits(enum.Enum):
    Celsius = 1
    Fahrenheit = 2


class Temperature:
    def __init__(self, value, units=TemperatureUnits.Celsius):
        if units == TemperatureUnits.Celsius:
            self.celsiusValue = value
        
        elif units == TemperatureUnits.Fahrenheit:
            self.celsiusValue = (value - 32.0) * (5.0/9.0)
        else:
            raise Exception("Invalid Temperature Unit Specified")
    def getCelsiusValue(self):
        return self.celsiusValue
    def getFahrenheitValue(self):
        return self.celsiusValue * (9.0/5.0) + 32.0


def main():
    for i in range(3):
        f = float(input("Enter the temperature in Fahrenheit: "))
        temperature = Temperature(f, units=TemperatureUnits.Fahrenheit)
        print("The temperature in Celsius is", temperature.getCelsiusValue(),
          "degrees")


if __name__ == "__main__":
    main()
