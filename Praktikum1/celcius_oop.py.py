class SuhuCelcius:
    def __init__(self, celcius):
        self.celcius = celcius

    def farenheit(self):
        return (self.celcius * 9/5) + 32
    def reamur(self):
        return (self.celcius * 4/5)
    def kelvin(self):
        return (self.celcius + 273.15)
    print("Suhu Celcius")
    
celcius1 = SuhuCelcius(75)
print(f"Konversi dari Celcius ke Farenheit: {celcius1.farenheit()}")
celcius2 = SuhuCelcius(60)
print(f"Konversi dari Celcius ke Reamur: {celcius2.reamur()}")
celcius3 = SuhuCelcius(90)
print(f"Konversi dari Celcius ke Kelvin: {celcius3.kelvin()}")
print("="*50)