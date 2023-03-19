#Yeyet Nurul Hayati_210511158
#Contoh 3

class Lingkaran:
       def __init__(self, jari_jari):
              self.jari_jari = jari_jari

       def luas(self):
              return 3.14 * (self.jari_jari ** 2)

lingkaranA = Lingkaran(35)
print(f"Luas lingkaran: {lingkaranA.luas()}")