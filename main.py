class Converter:
    def celFah(self, celsius: float) -> float:
        fahrenheit = (celsius * (9 / 5)) + 32
        return fahrenheit

    def fahCel(self, fahrenheit: float) -> float:
        celsius = round((fahrenheit - 32) * (5 / 9), 2)
        return celsius

    def celKel(self, celsius: float) -> float:
        kelvin = celsius + 273.15
        return kelvin

    def kelCel(self, kelvin: float) -> float:
        celsius = round(kelvin - 273.15, 2)
        return celsius

    def fahKel(self, fahrenheit: float) -> float:
        kelvin = round((fahrenheit - 32) * (5 / 9) + 273.15, 2)
        return kelvin

    def kelFah(self, kelvin: float) -> float:
        fahrenheit = round((kelvin * 9 / 5) - 459.67, 2)
        return fahrenheit
