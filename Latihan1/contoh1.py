#Yeyet Nurul Hayati_210511158
#Contoh 1

class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

mobilA = Mobil("sport","Ungu")
mobilA.info() # Output: Mobil sport berwarna ungu


