# Nama : Yeyet Nurul Hayati
# NIM   : 210511158
# Kelas : Karyawan

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def perkenalan(self):
        print("Perkenalkan nama saya adalah", self.nama)
class Kelas(Mahasiswa):
    def __init__(self, nama, jk, kelas):
        super().__init__(nama, jk)
        self.kelas = kelas
    def biodata(self):
        print("Nama  :",self.nama,"\nNIM   :",self.nim,"\nKelas :",self.kelas)
kelasA = Kelas("Yeyet Nurul Hayati", "210511158", "Karyawan")
kelasA.perkenalan() 
kelasA.biodata()