#Yeyet Nurul Hayati_210511158
#Contoh 7

class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
    
mycelcius = 80
mykelvin = Celcius.to_kelvin(mycelcius)
print(mykelvin)