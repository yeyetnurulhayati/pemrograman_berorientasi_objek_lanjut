#Yeyet Nurul Hayati_210511158_PBOK2
#Contoh 2

class Mahasiswa:
     def __init__(self, nama, npm):
       self.nama = nama
       self.npm = npm

     def info(self):
          print(f"Nama: {self.nama}\nNPM: {self.npm}")

mahasiswaB = Mahasiswa("Yeyet Nurul Hayati", "2105111158")
mahasiswaB.info()